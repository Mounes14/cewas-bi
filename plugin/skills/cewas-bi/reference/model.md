# cewas EDP model - reference

Model `ac05b981-5411-4371-aa3f-659a5a933f0d` (workspace "EDS PowerBI"). Read-only.

## Tables
| Table | Use | Notes |
|---|---|---|
| **Diagnostic** | The EDS surveys. One row = one survey round of one enterprise; one column per question (≈495 columns) | Source: Dataverse `cewasEDP_DiagnosticData` |
| **Program** | Programme master: `ProgramName`, `Program Type` (Acceleration / Incubation / Scale Up), `Country`, `start_date`, `end_date` | Related: `Diagnostic[ProgramName]` → `Program[ProgramName]` (many-to-one). Many programmes have no dates |
| **Contacts** | People: `Full Name`, `Email`, `Job Title`, `Organization Name`, `Created On` | Not related to Diagnostic; join on email only if asked |
| Date | Calendar | Rarely needed |
| ~~Old Data~~, ~~Old_programs~~ | **Ignore** | Legacy |

## Key Diagnostic columns
| Column | Meaning |
|---|---|
| `cewasEDP_DEV` | Record ID (GUID) of the survey row - unique. Use it to target one survey |
| `MatchingID` | EDS export ID like `cewasEDP-001090` - blank on older rows, do not rely on it |
| `Enterprise` | Enterprise name (messy: spaces, case, typos) |
| `Info_Contact_Email` | Contact email - part of the enterprise identity |
| `Status` | `Pre`, `Post1`, `Post2`, `Post Final` |
| `ProgramName` | Programme (can be blank on some Post rows) |
| `Created On` / `Modified On` | Survey created / last edited (date-time) |
| `Rated by` | cewas staff member who scored the survey |
| `Submitted by`, `createdbyname` | Who created the record (portal user, or "Red IT" for system-created rows) |
| `EDP_Total_Score` | Overall EDS score 0-100. **Stored as TEXT → use `VALUE(Diagnostic[EDP_Total_Score])`** for maths/sorting |
| `Info_Country`, `Info_City`, `Info_CEO`, `Info_Website`, `Info_Main_contact_role`, `Info_Short_description` | Enterprise profile (country spelling varies, e.g. "Jordan", "الأردن") |
| `secondRound_evaluation`, `Confirmation` | Yes/No flags |

### Score columns (naming)
- **Section scores (%)**: `<section>_rating_percent` (0-100, the % shown in the EDS PDF), plus `_rating_total` (points) and `_maxscore`. Segment columns: `proofofbusinessconcept_rating_percent`, `marketsuccessthroughinnovation_rating_percent`, `managementandfinancing_rating_percent`, `capacitytodeliver_rating_percent`, `impactpotential_rating_percent`. All areas/topics: see questions.md headings.
- **Question scores (points)**: `<question>_rating`, 0..1 (SDG 2: 0..0.3). 62 of them carry a `redit_` prefix (e.g. `redit_pricing_clearpricing_rating`); SDG ones are lowercase without dots (`impact_sdg61_rating`). Always take the exact name from questions.md.
- A **blank** question score = not yet rated (counts as 0 in the section %).

### Answer columns
- Readable answer columns are listed in questions.md (`Answer column`). Numbers are numbers, Yes/No as text, choices as text.
- Columns prefixed `redit_` / `cr87e_` (without `_rating`) hold **option codes** for the same answer (e.g. `redit_businessplankpis_businessplan` = 119960001). Booleans: `-1` = Yes, `0` = No (`redit_*`), `True/False` (`cr87e_*`).
- Multi-select answers are stored **only as code lists** (`lettingothersdothework_outsource`, `solvingsectorchallenges_barriers`, `contributionstatustype_aspects`, `impactmgmt_measuremonitor`, `investmentneedsandoptions_type`, `customerseg_type`): decode each code with option_labels.json.

## Identity and comparison rules
- Same enterprise = same normalised `Enterprise` + `Info_Contact_Email` (normalise = lower-case, trim, collapse spaces, drop punctuation); blank email on a row → name alone. Never merge different names (different words = different enterprises).
- Progress = Pre vs Post Final. All rounds only when asked how many/which rounds.

## DAX patterns (replace names/IDs)
Find an enterprise and its rounds:
```
EVALUATE
SELECTCOLUMNS(
  FILTER(Diagnostic, CONTAINSSTRING(Diagnostic[Enterprise], "aman grow")),
  "ID", Diagnostic[cewasEDP_DEV], "Enterprise", Diagnostic[Enterprise], "Email", Diagnostic[Info_Contact_Email],
  "Status", Diagnostic[Status], "Programme", Diagnostic[ProgramName], "Created", Diagnostic[Created On],
  "Rated by", Diagnostic[Rated by], "Total", VALUE(Diagnostic[EDP_Total_Score]))
ORDER BY [Created]
```
Segment scores of selected surveys:
```
EVALUATE
SELECTCOLUMNS(
  FILTER(Diagnostic, Diagnostic[cewasEDP_DEV] IN {"<id1>", "<id2>"}),
  "Status", Diagnostic[Status], "Total", VALUE(Diagnostic[EDP_Total_Score]),
  "Proof of Business Concept", Diagnostic[proofofbusinessconcept_rating_percent],
  "Market Success through Innovation", Diagnostic[marketsuccessthroughinnovation_rating_percent],
  "Management and Financing", Diagnostic[managementandfinancing_rating_percent],
  "Capacity to deliver", Diagnostic[capacitytodeliver_rating_percent],
  "Impact Potential", Diagnostic[impactpotential_rating_percent])
```
Answers + scores of one topic (columns from questions.md), e.g. impact figures:
```
EVALUATE
SELECTCOLUMNS(FILTER(Diagnostic, Diagnostic[cewasEDP_DEV] IN {"<pre>", "<post>"}),
  "Status", Diagnostic[Status], "People benefiting", Diagnostic[impact_peoplebenefiting],
  "SDG 6.2 new access", Diagnostic[Impact_SDG6.2], "SDG 13 GHG avoided (t)", Diagnostic[Impact_SDG13])
```
Enterprises per programme (then apply the identity rule to count unique enterprises):
```
EVALUATE
SUMMARIZECOLUMNS(Diagnostic[ProgramName], Diagnostic[Enterprise], Diagnostic[Info_Contact_Email], Diagnostic[Status],
  FILTER(VALUES(Diagnostic[ProgramName]), CONTAINSSTRING(Diagnostic[ProgramName], "GGGI")),
  "Surveys", COUNTROWS(Diagnostic))
```
Programme list with type/country/dates:
```
EVALUATE SELECTCOLUMNS(Program, "Programme", Program[ProgramName], "Type", Program[Program Type],
  "Country", Program[Country], "Start", Program[start_date], "End", Program[end_date])
```
Cohort progress (Pre vs Post Final averages): pull Enterprise, Email, Status, total and segment scores for the programme's Pre and Post Final rows, pair them with the identity rule, and average only enterprises that have both.

## Counts at a glance (Oct-2026, for orientation only - always query live)
322 surveys; Status: Pre 189, Post Final 126, Post1 6, Post2 1; 26 programmes in Program table.
