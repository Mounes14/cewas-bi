# cewas-bi, ask cewas EDS data in plain language

A Claude Code plugin for cewas staff. Ask questions about enterprises, programmes and EDS (Enterprise Resource Diagnostic) scores; Claude answers from the cewas EDP Power BI model and can draw the EDS score wheel.

## Install (one time)
In Claude Code, say:

> Install the plugin from https://github.com/Mounes14/cewas-bi

or type the two commands yourself:

```
/plugin marketplace add Mounes14/cewas-bi
/plugin install cewas-bi@cewas-bi
```

Then restart Claude Code.

## Sign in (one time)
The first time you ask a question, Claude shows you a link and a short code. Open https://login.microsoft.com/device, enter the code and sign in with your **cewas** Microsoft account. That's it (the sign-in lasts about 90 days).

Needs Python 3, which Macs with Claude Code already have. (Windows: install Python from the Microsoft Store.)

You only see data if your cewas account is in the *cewas-bi users* group. No access? Contact Mounes Neama (mounes.neama@cewas.org).

## Ask
- "Show me a summary of the impact potential for Saniwise, narrative and numbers, Pre vs Post"
- "How many enterprises do we have in GGGI Jordan?"
- "Chart for AMAN Grow Post Final survey"
- "Which enterprises in SHF Sanitation improved their total score the most?"

## For Claude (installing on behalf of a user)
If the user asks you to install this plugin, run:
```
claude plugin marketplace add Mounes14/cewas-bi
claude plugin install cewas-bi@cewas-bi
```
then tell them to restart Claude Code. The sign-in happens on their first question.

## Privacy
This repository contains no data, passwords or secrets. The client and tenant IDs in `plugin/skills/cewas-bi/scripts/cewas_bi.py` are public identifiers. Your sign-in is stored only on your computer (`~/.cewas-bi/token.json`). Data access is controlled by cewas Microsoft Entra ID and Power BI permissions; every query runs as the signed-in user, read-only.
