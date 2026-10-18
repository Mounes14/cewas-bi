#!/usr/bin/env python3
"""cewas-bi helper: query the cewas EDP Power BI model (REST executeQueries) as the signed-in user.

Standard library only (no pip installs). Works with Python 3.8+.

  login                     one-time sign-in (device code, cewas Microsoft account)
  whoami                    show the signed-in account
  logout                    forget the sign-in on this computer
  query  --dax "EVALUATE ..." | --dax-file F   [--csv PATH] [--json] [--max-print 40]
  chart  --id <cewasEDP_DEV> [--compare <cewasEDP_DEV> | --no-compare] [--out PATH] [--no-open]

Exit codes: 0 ok, 2 not signed in, 3 access denied, 4 query error, 5 network error.
"""
import argparse, base64, csv, datetime, json, os, re, ssl, subprocess, sys, time
import urllib.error, urllib.parse, urllib.request

TENANT = "c0924178-b957-4f3d-beec-db355a1a8da6"          # cewas Microsoft tenant (public identifier)
CLIENT_ID = "de3191cb-c7aa-435f-a403-62b31ee5ff38"       # cewas-bi (Claude) app: public client, no secret
WORKSPACE = "adc538ea-1104-42c8-af61-4de337322274"       # EDS PowerBI
MODEL = "ac05b981-5411-4371-aa3f-659a5a933f0d"           # cewas EDP semantic model
SCOPE = "https://analysis.windows.net/powerbi/api/.default offline_access openid profile"
AUTH = "https://login.microsoftonline.com/%s/oauth2/v2.0" % TENANT
API = "https://api.powerbi.com/v1.0/myorg/groups/%s/datasets/%s/executeQueries" % (WORKSPACE, MODEL)
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
STATE_DIR = os.path.join(os.path.expanduser("~"), ".cewas-bi")
TOKEN_FILE = os.path.join(STATE_DIR, "token.json")
CONTACT = "Mounes Neama (mounes.neama@cewas.org)"


# ---------------------------------------------------------------- http helpers
def _ctx():
    try:
        return ssl.create_default_context()
    except Exception:  # pragma: no cover
        return None


def _post(url, data, headers=None, form=True, timeout=120):
    body = urllib.parse.urlencode(data).encode() if form else json.dumps(data).encode()
    h = {"Content-Type": "application/x-www-form-urlencoded" if form else "application/json"}
    h.update(headers or {})
    req = urllib.request.Request(url, data=body, headers=h, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_ctx()) as r:
            return r.status, json.loads(r.read().decode("utf-8-sig") or "{}")
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, {"raw": raw[:1500]}
    except urllib.error.URLError as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e):
            sys.exit("Network/SSL error: Python cannot verify certificates. On Mac run "
                     "'/Applications/Python*/Install Certificates.command' or use /usr/bin/python3. (%s)" % e)
        print("Network error: %s" % e, file=sys.stderr)
        sys.exit(5)


# ---------------------------------------------------------------- token cache
def _save(tok):
    if not os.path.isdir(STATE_DIR):
        os.makedirs(STATE_DIR, mode=0o700)
    tok["saved_at"] = time.time()
    fd = os.open(TOKEN_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(tok, f)


def _load():
    try:
        with open(TOKEN_FILE) as f:
            return json.load(f)
    except (IOError, ValueError):
        return None


def _claims(tok):
    try:
        p = tok["id_token"].split(".")[1]
        p += "=" * (-len(p) % 4)
        return json.loads(base64.urlsafe_b64decode(p))
    except Exception:
        return {}


def access_token():
    tok = _load()
    if not tok or "refresh_token" not in tok:
        print("NOT_SIGNED_IN: run the 'login' command first.", file=sys.stderr)
        sys.exit(2)
    if time.time() < tok.get("saved_at", 0) + tok.get("expires_in", 0) - 300:
        return tok["access_token"]
    st, new = _post(AUTH + "/token", {"client_id": CLIENT_ID, "grant_type": "refresh_token",
                                      "refresh_token": tok["refresh_token"], "scope": SCOPE})
    if st != 200 or "access_token" not in new:
        print("NOT_SIGNED_IN: sign-in expired (%s). Run the 'login' command again." %
              new.get("error_description", new)[:300], file=sys.stderr)
        sys.exit(2)
    new.setdefault("id_token", tok.get("id_token"))
    new.setdefault("refresh_token", tok["refresh_token"])
    _save(new)
    return new["access_token"]


# ---------------------------------------------------------------- commands
def cmd_login(_):
    st, flow = _post(AUTH + "/devicecode", {"client_id": CLIENT_ID, "scope": SCOPE})
    if st != 200 or "user_code" not in flow:
        sys.exit("Could not start sign-in: %s" % json.dumps(flow)[:800])
    print("SIGN-IN: open %s and enter the code %s (use your cewas Microsoft account). Waiting up to %d minutes..."
          % (flow["verification_uri"], flow["user_code"], int(flow.get("expires_in", 900)) // 60), flush=True)
    interval, deadline = int(flow.get("interval", 5)), time.time() + int(flow.get("expires_in", 900))
    while time.time() < deadline:
        time.sleep(interval)
        st, tok = _post(AUTH + "/token", {"client_id": CLIENT_ID, "device_code": flow["device_code"],
                                          "grant_type": "urn:ietf:params:oauth:grant-type:device_code"})
        if st == 200 and "access_token" in tok:
            _save(tok)
            c = _claims(tok)
            print("LOGIN OK as %s" % (c.get("preferred_username") or c.get("upn") or "?"))
            return
        err = tok.get("error")
        if err == "slow_down":
            interval += 5
        elif err != "authorization_pending":
            sys.exit("Sign-in failed: %s" % tok.get("error_description", tok)[:600])
    sys.exit("Sign-in timed out. Run login again.")


def cmd_whoami(_):
    tok = _load()
    if not tok:
        print("Not signed in.")
        sys.exit(2)
    c = _claims(tok)
    print("Signed in as %s" % (c.get("preferred_username") or c.get("upn") or "?"))


def cmd_logout(_):
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)
    print("Signed out on this computer.")


def run_dax(dax):
    st, j = _post(API, {"queries": [{"query": dax}], "serializerSettings": {"includeNulls": True}},
                  headers={"Authorization": "Bearer " + access_token()}, form=False, timeout=300)
    if st in (401, 403):
        print("ACCESS_DENIED (HTTP %d): your account cannot read the cewas EDP model. Ask %s to add you to the "
              "'cewas-bi users' group. Details: %s" % (st, CONTACT, json.dumps(j)[:400]), file=sys.stderr)
        sys.exit(3)
    if st != 200:
        detail = json.dumps(j)
        m = re.search(r'"value":\s*"([^"]+)"', detail)
        print("QUERY_ERROR (HTTP %d): %s" % (st, m.group(1) if m else detail[:1500]), file=sys.stderr)
        sys.exit(4)
    res = j["results"][0]
    if res.get("error"):
        print("QUERY_ERROR: %s" % json.dumps(res["error"])[:1500], file=sys.stderr)
        sys.exit(4)
    return res["tables"][0]["rows"]


def _clean(col):  # "Diagnostic[Status]" -> "Status", "[Total]" -> "Total"
    m = re.match(r"^.*?\[(.*)\]$", col)
    return m.group(1) if m else col


def _downloads():
    d = os.path.join(os.path.expanduser("~"), "Downloads")
    return d if os.path.isdir(d) else os.path.expanduser("~")


def cmd_query(a):
    dax = a.dax if a.dax else open(a.dax_file, encoding="utf-8").read()
    rows = run_dax(dax)
    if a.json:
        print(json.dumps([{_clean(k): v for k, v in r.items()} for r in rows], ensure_ascii=False))
        return
    if not rows:
        print("(0 rows)")
        return
    cols = list(rows[0].keys())
    names = [_clean(c) for c in cols]
    path = a.csv
    if not path and len(rows) > a.max_print:
        path = os.path.join(_downloads(), "cewas_bi_%s.csv" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    if path:
        with open(os.path.expanduser(path), "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(names)
            for r in rows:
                w.writerow([r.get(c) for c in cols])
        print("CSV: %s (%d rows)" % (path, len(rows)))

    def fmt(v):
        if v is None:
            return ""
        if isinstance(v, float):
            return ("%.2f" % v).rstrip("0").rstrip(".") if abs(v) < 1000 else "{:,.0f}".format(v)
        return str(v).replace("\n", " ").replace("|", "/")

    show = rows if not path else rows[:10]
    print("| " + " | ".join(names) + " |")
    print("|" + "---|" * len(names))
    for r in show:
        print("| " + " | ".join(fmt(r.get(c)) for c in cols) + " |")
    if path and len(rows) > 10:
        print("... first 10 of %d rows shown; all rows in the CSV" % len(rows))


def _q(s):
    return '"%s"' % str(s).replace('"', '""')


def cmd_chart(a):
    cols = ("Enterprise", "Info_Contact_Email", "Status", "ProgramName", "Info_Country", "Created On", "Rated by",
            "EDP_Total_Score", "cewasEDP_DEV")
    sel = ", ".join('"%s", Diagnostic[%s]' % (c, c) for c in cols)
    meta = run_dax("EVALUATE SELECTCOLUMNS(FILTER(Diagnostic, Diagnostic[cewasEDP_DEV] = %s), %s)" % (_q(a.id), sel))
    if not meta:
        sys.exit("No survey with cewasEDP_DEV = %s" % a.id)
    m = {_clean(k): v for k, v in meta[0].items()}

    cmp_id = None if a.no_compare else a.compare
    if not cmp_id and not a.no_compare and m["Status"] != "Pre":
        # same enterprise = same normalised name + email (blank email -> name only)
        same = run_dax("EVALUATE SELECTCOLUMNS(FILTER(Diagnostic, LOWER(TRIM(Diagnostic[Enterprise])) = %s && "
                       "Diagnostic[Status] = \"Pre\"), %s)" % (_q((m["Enterprise"] or "").strip().lower()), sel))
        em = (m.get("Info_Contact_Email") or "").strip().lower()
        for r in same:
            r = {_clean(k): v for k, v in r.items()}
            e2 = (r.get("Info_Contact_Email") or "").strip().lower()
            if not em or not e2 or em == e2:
                cmp_id = r["cewasEDP_DEV"]
                break
    cmp_meta = None
    if cmp_id:
        cm = run_dax("EVALUATE SELECTCOLUMNS(FILTER(Diagnostic, Diagnostic[cewasEDP_DEV] = %s), %s)" % (_q(cmp_id), sel))
        cmp_meta = {_clean(k): v for k, v in cm[0].items()} if cm else None

    dax = open(os.path.join(SKILL, "reference", "chart_query.dax"), encoding="utf-8").read()
    dax = dax.replace("__ID__", a.id).replace("__CMP__", cmp_id or "")
    rows = [[int(r["[o]"]), r.get("[s]"), r.get("[p]") if cmp_id else None, int(r.get("[u]") or 0)]
            for r in run_dax(dax)]
    unscored = sum(r[3] for r in rows)

    def num(v):
        try:
            return round(float(v), 2)
        except (TypeError, ValueError):
            return None

    notes = ["Source: Power BI cewas EDP, Diagnostic table" + (" (comparison: %s survey)." % cmp_meta["Status"]
                                                               if cmp_meta else ".")]
    if unscored:
        notes.append("%d scored question(s) have no rating yet in this survey; their sections read lower "
                     "until they are scored." % unscored)
    data = {"enterprise": (m["Enterprise"] or "").strip(), "status": m["Status"], "program": m["ProgramName"],
            "country": m["Info_Country"], "date": (m["Created On"] or "")[:10], "rated_by": m["Rated by"],
            "total": num(m["EDP_Total_Score"]), "compare_label": cmp_meta["Status"] if cmp_meta else None,
            "compare_total": num(cmp_meta["EDP_Total_Score"]) if cmp_meta else None, "rows": rows, "notes": notes}
    html = open(os.path.join(SKILL, "templates", "eds_sunburst.html"), encoding="utf-8").read()
    html = html.replace("/*DATA*/", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    safe = re.sub(r"[^\w\-]+", "_", "%s_%s" % (data["enterprise"], data["status"])).strip("_")
    out = os.path.expanduser(a.out) if a.out else os.path.join(_downloads(), "EDS_%s.html" % safe)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("CHART: %s" % out)
    print(json.dumps({"enterprise": data["enterprise"], "status": data["status"], "total": data["total"],
                      "compare": data["compare_label"], "compare_total": data["compare_total"],
                      "unscored_questions": unscored}, ensure_ascii=False))
    if not a.no_open:
        opener = {"darwin": ["open"], "win32": ["cmd", "/c", "start", ""]}.get(sys.platform, ["xdg-open"])
        try:
            subprocess.Popen(opener + [out], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except OSError:
            pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("login")
    sub.add_parser("whoami")
    sub.add_parser("logout")
    q = sub.add_parser("query")
    g = q.add_mutually_exclusive_group(required=True)
    g.add_argument("--dax")
    g.add_argument("--dax-file")
    q.add_argument("--csv")
    q.add_argument("--json", action="store_true")
    q.add_argument("--max-print", type=int, default=40)
    c = sub.add_parser("chart")
    c.add_argument("--id", required=True)
    c.add_argument("--compare")
    c.add_argument("--no-compare", action="store_true")
    c.add_argument("--out")
    c.add_argument("--no-open", action="store_true")
    a = ap.parse_args()
    if not a.cmd:
        ap.print_help()
        return
    {"login": cmd_login, "whoami": cmd_whoami, "logout": cmd_logout, "query": cmd_query, "chart": cmd_chart}[a.cmd](a)


if __name__ == "__main__":
    main()
