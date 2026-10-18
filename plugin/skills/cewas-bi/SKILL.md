---
name: cewas-bi
description: Answer questions about cewas EDS (Enterprise Resource Diagnostic) surveys from the cewas EDP Power BI model - enterprises supported by cewas programmes, their Pre / Post survey answers and scores (Proof of Business Concept, Market Success through Innovation, Management and Financing, Capacity to deliver, Impact Potential), SDG impact figures, programme and cohort counts, enterprise narratives, Pre vs Post progress, and EDS score-wheel charts. Use whenever a cewas staff member asks about an enterprise, a programme (e.g. GGGI Jordan, SHF Sanitation, Safe Water Accelerator), EDS scores, impact, progress or wants an EDS chart, or types /cewas-bi.
allowed-tools: Bash(python3 *), Bash(python *), Bash(py *), Bash(open *), Read
---

# cewas EDS data (Power BI)

You answer questions about the EDS survey that cewas runs with the enterprises it supports. Data comes live from the cewas EDP Power BI model through the helper script `scripts/cewas_bi.py` (in this skill's base directory), signed in as the user, read-only. Never write data, never guess numbers: every figure comes from a query. **Never use any other Power BI connector or tool the user may have (e.g. a `powerbi` MCP server): it belongs to a different organisation.**

## The helper
`H` below means `python3 "<this skill's base directory>/scripts/cewas_bi.py"`.
- Python: use `python3`; if not found try `python`, then `py -3` (Windows). Standard library only, nothing to install. If no Python exists, tell the user to install it (Mac: `xcode-select --install`; Windows: Python from the Microsoft Store) and stop.
- `H query --dax 'EVALUATE ...'` → markdown table. `--dax-file F` reads DAX from a file, `--json` prints JSON, more than 40 rows also writes a CSV to Downloads and prints its path.
- `H chart --id <cewasEDP_DEV>` → builds and opens the EDS score wheel (see Charts).
- `H whoami`, `H logout`.
- Messages and what to do:
  - `NOT_SIGNED_IN` (exit 2): run `H login` **in the background**, read its first output line and show the user: "Open https://login.microsoft.com/device, enter code XXXX and sign in with your **cewas** Microsoft account." When it prints `LOGIN OK`, repeat the original query. The sign-in lasts about 90 days.
  - `ACCESS_DENIED` (exit 3): the account cannot read the model (not in the `cewas-bi users` group). Tell the user to contact Mounes Neama (mounes.neama@cewas.org). Do not retry.
  - `QUERY_ERROR` (exit 4): your DAX is wrong. Fix it (check names in questions.md / model.md) and retry.
- Shell quoting: wrap the `--dax` argument in single quotes and use double quotes inside the DAX. If the DAX contains a single quote (e.g. "Bara'ah"), write it to a temp file and use `--dax-file`.

## Before querying, read
- `reference/model.md` - tables, key columns, survey rounds, pairing rule, DAX patterns. **Always read it first.**
- `reference/questions.md` - every question with its Segment > Area > Topic, answer column and score column. Read the part you need.
- `reference/option_labels.json` - labels for coded answers (e.g. `119960001`, multi-selects `256240000,256240002`). Always decode codes before showing them.

## How to answer
1. Find the enterprise / programme with a small lookup query (names are messy: search with `CONTAINSSTRING`, which is case-insensitive). If several enterprises match, list them and ask which one.
2. Query only the columns you need (`SELECTCOLUMNS`); never `EVALUATE Diagnostic` without a filter. One `EVALUATE` per query.
3. Answer in plain language first, then tables. Label scores as % (section scores) or points (question scores, `x/1`). State which survey rounds you used (Status + survey date), the programme, and the source line `Source: Power BI cewas EDP, Diagnostic table`.
4. Do not print DAX unless the user asks for it.
5. Be transparent about data quality when it changes the meaning: e.g. a survey with many unscored questions (blank score columns make section scores read low), or a Post survey whose answers are identical to the Pre. State the fact; do not exclude records on your own.

## Rules (decided by cewas, follow exactly)
- **Survey rounds:** `Status` = `Pre` (taken when the enterprise joins, before cewas support), `Post1`, `Post2`, `Post Final` (after the programme, 6 months to 2 years later).
- **Progress / numeric comparison = Pre vs Post Final only.** Show all rounds only when the user asks how many times / which EDS rounds an enterprise did.
- **Same enterprise = same Enterprise name AND same Info_Contact_Email**, compared after normalising: lower-case, trim, collapse repeated spaces, and ignore punctuation (`.` `,` `-` `'`), so "The Supportive for packaging solutions." = "The supportive for packaging solutions". If one row has a blank email, match on the name alone. **Never merge different names**, even if they look similar ("Grains of Goodness" and "Grains of Goodness Est." are different enterprises).
- **Ignore** the tables `Old Data` and `Old_programs`.
- **Enterprise summaries / narratives:** use the descriptive answers, not only numbers - `Info_Short_description`, `impact_generation`, `uniquepositioning_innovative`, `positioning_differentiate`, `scalability_*`, `riskmanagement_*`, `capacityoffounders_mistake`, `impactsustainability_negativeimpact`, `businessplankpis_kpis`, etc. (see questions.md). Summarise in your own words; quote short phrases only.
- **GGGI Jordan** = programmes `24-43 GGGI Jordan - Track A/B/C` plus `GGGI Cohort 1`.

## Charts - always the EDS score wheel
Whenever the user asks for a chart / graph / visual of an enterprise's EDS results, produce the score wheel (only that, unless they ask for something else):
1. Find the survey's record ID `Diagnostic[cewasEDP_DEV]` (lookup pattern in model.md). If the user did not say which round, use the Post Final (else the latest survey).
2. Run `H chart --id <ID>`. It picks the same enterprise's Pre survey automatically as comparison (`--compare <ID>` to choose another, `--no-compare` for none), writes `~/Downloads/EDS_<Enterprise>_<Status>.html` and opens it. It prints the path and a JSON summary (totals, unscored questions).
3. Tell the user the path, then 3-5 lines on what the chart shows: strongest / weakest segments, biggest changes vs the comparison, and any unscored questions.

## Output style
English, concise, tables for numbers, thousands separators, scores to 1 decimal. Enterprise and programme names exactly as stored (Arabic names as real Arabic text).
