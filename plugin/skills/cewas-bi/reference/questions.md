# EDS question map

Hierarchy: Segment > Area > Topic > Question. Section scores: `<section>_rating_percent` (0-100, as shown in the EDS PDF).
Question score columns are 0..max (max = 1, except SDG 2 = 0.3). "n/r" = not rated (descriptive only).
Answer column = readable answer (text/number/Yes-No). Codes for choice/multi-select answers: see option_labels.json.


## Proof of Business Concept  — `proofofbusinessconcept_rating_percent`
### Market potential  — `marketpotential_rating_percent`
#### Customer Segmentation  — `customerseg_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Do you (mainly) target end-customers (B2C), other businesses (B2B), governments (B2G) or donor organizations (B2D)? | `customerseg_type` | n/r |
| Which customer segments do you target and how many have you served in the last calendar year (per customer type)? | `customerseg_segmentsserved` | `customerseg_segmentsserved_rating` (1) |
| Have you conducted a needs assessment of your end users and adapted your offers according to the results? If yes, describe what you did. | `customerseg_needsassessment` | `customerseg_needsassessment_rating` (1) |
#### Market size  — `marketsize_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| How large is your current SAM (serviceable target market) in terms of total number of customers? | `marketsize_SAM` | `marketsize_sam_rating` (1) |
| What assumptions went into your SAM projections? | `marketsize_assumptions` | `marketsize_assumptions_rating` (1) |
| How large is your current target market in terms of revenue you can generate per year in US$ equivalent? (# of your potential customers multiplied by the average annual revenue generated per customer) | `marketsize_revenuetargetmarket` | `marketsize_revenuetargetmarket_rating` (1) |
| Which factors drive the development of your market? | `marketsize_developmentfactors` | `marketsize_developmentfactors_rating` (1) |
#### Positioning  — `positioning_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Is your business model built around product(s), service(s) or a combination thereof? | `positioning_businessmodell` | n/r |
| Which of the following statements best describes the status of your most advanced product or service? | `positioning_statusproductservice` | `redit_positioning_statusproductservice_rating` (1) |
| Who are your competitors (both direct and indirect), and what solutions do they offer? | `positioning_competitor` | `redit_positioning_competitors_rating` (1) |
| How do you differentiate yourself from your competition? | `positioning_differentiate` | `redit_positioning_differentiate_rating` (1) |
#### Pricing  — `pricing_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Have you established clear pricing of your products or services? | `pricing_clearpricing` | `redit_pricing_clearpricing_rating` (1) |
| Do you (plan to) generate repeat sales or regular revenues from your customers? | `pricing_generate` | `redit_pricing_generate_rating` (1) |
#### Marketing resources  — `marketingresources_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Do you have a marketing plan and budget? | `marketingresources_planbudget` | `redit_marketingresources_planbudget_rating` (1) |
| Do you use a Customer Relationship Management (CRM) system? | `marketingresources_crm` | `redit_marketingresources_crm_rating` (1) |
| Do you have documented customer testimonials? | `marketingresources_testimonials` | `redit_marketingresources_testimonials_rating` (1) |
### Revenue generation  — `revenuegeneration_rating_percent`
#### Sales track record  — `salestrackrecord_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Since when are you generating regular revenues from the sales of your product(s) and/or service(s) | `salestrackrecord_revenues` | `redit_salestrackrecord_revenues_rating` (1) |
| How much revenue have you generated during the last financial year (total turnover) in USD? | `salestrackrecord_totalturnover` | `redit_salestrackrecord_totalturnover_rating` (1) |
| How much revenue have you generated from direct sales during the last six months? | `salestrackrecord_directsales` | `redit_salestrackrecord_directsales_rating` (1) |
| Have your revenues continuously increased each month during the last six months? | `salestrackrecord_increasedrevenues` | `redit_salestrackrecord_increasedrevenues_rating` (1) |
#### Profitability  — `profitability_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| How much profit or loss do you currently generate per customer with your most profitable product and/or service? | `profitability_profitloss` | `redit_profitability_profitloss_rating` (1) |
| When do you plan to break even? | `profitability_breakeven` | `redit_profitability_breakeven_rating` (1) |
| How accurate has your sales forecast been in the past 6 months? | `profitability_forecast` | `redit_profitability_forecast_rating` (1) |

## Market Success through Innovation  — `marketsuccessthroughinnovation_rating_percent`
### Business model innovation  — `businessmodelinnovation_rating_percent`
#### Unique positioning  — `uniquepositioning_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Why is your business model innovative and how does it uniquely solve your customers problem compared to the alternatives? | `uniquepositioning_innovative` | `redit_uniquepositioning_innovative_rating` (1) |
| Do you combine sales of your main product or service with complementary operation and maintenance or after sales services (that your competitors do not offer)? | `uniquepositioning_combinesales` | `redit_uniquepositioning_combinesales_rating` (1) |
| Does your business model (at least in part) build on a solution that has proven successful in other sectors but has not been applied in your target market / sector? | `uniquepositioning_businessmodel` | `redit_uniquepositioning_businessmodel_rating` (1) |
| Intellectual property: Have you patented your product(s)? | `uniquepositioning_intellectualproperty` | `redit_uniquepositioning_intellectualproperty_rating` (1) |
#### Scalability  — `scalability_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| What innovative aspects of your business model (could) make your business model scalable? | `scalability_scalable` | `redit_scalability_scalable_rating` (1) |
| What partnerships are key to scale your business model and impact? (please list them and explain what is the value proposition and incentives you offer them) | `scalability_partnerships` | `redit_scalability_partnerships_rating` (1) |
### Product innovation  — `productinnovation_rating_percent`
#### Solving sector challenges  — `solvingsectorchallenges_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Are you tackling any of the following barriers with your business model? | `solvingsectorchallenges_barriers` | `solvingsectorchallenges_barriers_rating` (1) |
| Do you offer innovative payment options (rate payments, success based payments, buy now pay later, etc.) that enable your customers to buy your product and/or service? If yes, please specify | `solvingsectorchallenges_payment` | `redit_solvingsectorchallenges_payment_rating` (1) |
### Process innovation  — `processinnovation_rating_percent`
#### Optimizing internal processes  — `optimizinginternalprocesses_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Have you conducted an analysis of the most cost intensive steps in your value creation chain and taken action to reduce costs in the past year? | `optimizinginternalprocesses_analysis` | `redit_optimizinginternalprocesses_analysis_rating` (1) |
| Have you identified priority areas to improve the QUALITY of your production / delivery processes (e.g. improving the quality of the products or services or reducing negative environmental impacts of your production)? If yes, please specify: | `optimizinginternalprocesses_quality` | `redit_optimizinginternalprocesses_quality_rating` (1) |
#### Letting others do the work  — `lettingothersdothework_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| In which of the following areas do you outsource value creation (at least partly)? | `lettingothersdothework_outsource` | `redit_lettingothersdothework_outsource_rating` (1) |
| Do you engage / collaborate with customers in the value creation of the products/services your business offers? If yes, please specify: | `lettingothersdothework_customers` | `redit_lettingothersdothework_customers_rating` (1) |

## Management and Financing  — `managementandfinancing_rating_percent`
### Operational and strategic planning  — `operationalstrategicplanning_rating_percent`
#### Business plan & KPIs  — `businessplankpis_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Do you have a comprehensive, up to date business plan document? | `businessplankpis_businessplan` | `redit_businessplankpis_businessplan_rating` (1) |
| Have you established Key Performance Indicators (KPIs) and targets for your business? If yes, please share your KPIs and related targets for the current calendar year | `businessplankpis_kpis` | `redit_businessplankpis_kpis_rating` (1) |
| How (and how often) do you use and monitor progress against your KPIs and related annual targets? | `businessplankpis_monitor` | `redit_businessplankpis_monitor_rating` (1) |
#### Risk management  — `riskmanagement_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Which are the key risks your business is facing that could keep you from meeting your targets and what mitigation measures have you established? | `riskmanagement_risks` | `redit_riskmanagement_risks_rating` (1) |
| Have you assessed regulatory market barriers for your business? If yes, please specify which ones. | `riskmanagement_barriers` | `redit_riskmanagement_barriers_rating` (1) |
| What are your risk mitigation / coping measures to deal with any potential future financial distress? | `riskmanagement_financialdistress` | `redit_riskmanagement_financialdistress_rating` (1) |
### Financial management  — `financialmanagementsub_rating_percent`
#### Financial management  — `financialmanagementsubsub_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Do you have an updated and detailed financial plan available? | `financialmanagement_plan` | `redit_financialmanagement_plan_rating` (1) |
| Do you have a cash flow / liquidity management system? | `financialmanagement_liquidity` | `redit_financialmanagement_liquidity_rating` (1) |
#### Evidence  — `evidence_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| For how many years can you produce audited financial statements? | `evidence_financialstatements` | `redit_evidence_financialstatements_rating` (1) |
| Do you have a 1-3 page back-up documentation of your  financial model on your unit cost of your product/service available? | `evidence_documentation` | `redit_evidence_documentation_rating` (1) |
### Investments  — `investments_rating_percent`
#### Investment track record  — `investmenttrackrecord_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Total amount of grants received to date [in USD equivalent] | `investmenttrackrecord_grants` | `redit_investmenttrackrecord_grants_rating` (1) |
| Total amount of debt investment raised to date [in USD equivalent] | `investmenttrackrecord_debt` | `redit_investmenttrackrecord_debt_rating` (1) |
| Total amount of equity investment raised to date [in USD equivalent], | `investmenttrackrecord_equity` | `redit_investmenttrackrecord_equity_rating` (1) |
| Total amount of further investments (grants, debts, equity) under negotiations at the moment [USD equivalent] | `investmenttrackrecord_investments` | `redit_investmenttrackrecord_investments_rating` (1) |
| Has your business incurred any liabilities due to providing collateral for loans or other financial obligations? | `investmenttrackrecord_liabilities` | `redit_investmenttrackrecord_liabilities_rating` (1) |
| Has your company already been valuated by a third party? | `investmenttrackrecord_thirdparty` | `redit_investmenttrackrecord_thirdparty_rating` (1) |
#### Investment needs and options  — `investmentneedsandoptions_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| For how long is your liquidity secured? | `investmentneedsandoptions_liquidity` | `redit_investmentneedsandoptions_liquidity_rating` (1) |
| What is the amount of investments (not revenues!) do you seek to raise in the COMING twelve months? | `investmentneedsandoptions_amount` | `redit_investmentneedsandoptions_amount_rating` (1) |
| How much of the investment do you plan to use for what and what do you seek to achieve? | `investmentneedsandoptions_plan` | `redit_investmentneedsandoptions_plan_rating` (1) |
| What type of investment do you seek? | `investmentneedsandoptions_type` | `redit_investmentneedsandoptions_type_rating` (1) |

## Capacity to deliver  — `capacitytodeliver_rating_percent`
### Team composition  — `teamcomposition_rating_percent`
#### Capacity of founders  — `capacityoffounders_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| How many founders does your start-up have? | `capacityoffounders_howmanyfounders` | `redit_capacityoffounders_howmanyfounders_rating` (1) |
| Has at least one of the founders founded another enterprise before this one? | `capacityoffounders_before` | `redit_capacityoffounders_before_rating` (1) |
| Please provide an example of a mistake that happened during the past six months that you (and your team) learned from: | `capacityoffounders_mistake` | `redit_capacityoffounders_mistake_rating` (1) |
| For how long can you as a (team of) founder continue to work on your start-up with the salary level you are currently paying yourself(ves)? (insert # of months) | `capacityoffounders_salary` | `redit_capacityoffounders_salary_rating` (1) |
#### Team experience  — `teamexperience_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| How many people formally work in your enterprise in total (including founders, management and staff on a payslip)? | `teamexperience_peopleintotal` | `teamexperience_peopleintotal_rating` (1) |
| On average, how much practical experience do the operations managers have related to relevant technological aspects and work in the sector you target (e.g. water, sanitation, hygiene, waste, agriculture, etc.)? | `teamexperience_operationsmanagers` | `teamexperience_operationsmanagers_rating` (1) |
| On average, how much practical experience does your management team have related to financial management? | `teamexperience_financialmanagement` | `teamexperience_financialmanagement_rating` (1) |
| On average, how much practical experience do sales managers in your team have related to sales? | `teamexperience_salesmanagers` | `teamexperience_salesmanagers_rating` (1) |
| On average, how much practical experience do marketing managers in your team have related to marketing? | `teamexperience_marketingmanagers` | `teamexperience_marketingmanagers_rating` (1) |
| On average, how much practical experience do operations managers in your team have related to production processes? | `teamexperience_operationsmanagersproduction` | `teamexperience_operationsmanagersproduction_rating` (1) |
| On average, how many years of practical experience does the management team / founder(s) have in managing teams? | `teamexperience_managingteams` | `teamexperience_managingteams_rating` (1) |
#### Support network  — `supportnetwork_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| What is the highest level of external experiences and capacities that you can rely on? | `supportnetwork_highestlevel` | `supportnetwork_highestlevel_rating` (1) |
### Operational capacity  — `operationalcapacity_rating_percent`
#### Supply chain management  — `supplychainmgmt_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Are written agreements in place with key suppliers (e.g. for molds, etc.) and business partners? | `supplychainmgmt_writtenagreements` | `supplychainmgmt_writtenagreements_rating` (1) |
| Have you faced any supply gaps / interruptions that led to delays in your production or delivery of your product(s) or service(s) in the past six month? | `supplychainmgmt_interruptions` | `supplychainmgmt_interruptions_rating` (1) |
#### Production and delivery resources  — `productiondeliveryresources_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Have you established Standard Operating Procedures (SOPs) for your key operational processes? | `productiondeliveryresources_sop` | `productiondeliveryresources_sop_rating` (1) |
| Have you established all the necessary key resources to fully deliver your offering? (For product-based businesses, this includes fully functioning production facilities. For service-based businesses, this includes having the required people and resources in place). | `productiondeliveryresources_keyresources` | `productiondeliveryresources_keyresources_rating` (1) |
| By how much could you increase your production / delivery of services in the coming three months without additional external investments? | `productiondeliveryresources_increase` | `productiondeliveryresources_increase_rating` (1) |
### Governance  — `governance_rating_percent`
#### Legal setup and compliance  — `legalcompliance_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| As which type of legal entity have you established your business? | `legalcompliance_entitytype` | `legalcompliance_entitytype_rating` (1) |
| Do you have all required permits, licenses and approvals to operate? | `legalcompliance_permitslicenses` | `legalcompliance_permitslicenses_rating` (1) |
#### HR Management  — `hrmanagement_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Do you have written job descriptions for all team members? | `hrmanagement_jobdescriptions` | `hrmanagement_jobdescriptions_rating` (1) |
| Have you established a clear performance management framework to ensure accountability and appropriate compensation? | `hrmanagement_performancemanagement` | `hrmanagement_performancemanagement_rating` (1) |
| Do you have a succession plan for key positions? | `hrmanagement_successionplan` | `hrmanagement_successionplan_rating` (1) |
| Have you established a board that oversees the company and management team? | `hrmanagement_board` | `hrmanagement_board_rating` (1) |

## Impact Potential  — `impactpotential_rating_percent`
### What impact  — `whatimpact_rating_percent`
#### Status and type of contribution  — `contributionstatustype_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Please explain how you generate impact | `impact_generation` | n/r |
| Which of the following statements applies best when it comes to development problems you are tackling and your vision for solving them? | `contributionstatustype_developmentproblems` | `contributionstatustype_developmentproblems_rating` (1) |
| Is your business model contributing to any of the following aspects? | `contributionstatustype_aspects` | `contributionstatustype_aspects_rating` (1) |
#### Impact management  — `impactmgmt_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Have you defined impact related performance objectives or targets for this year? If yes, please share them. | `impactmgmt_performanceobjectives` | `impactmgmt_performanceobjectives_rating` (1) |
| Do you have an impact model or theory of change? | `impactmgmt_impactmodel` | `impactmgmt_impactmodel_rating` (1) |
| How regularly do you review your impact strategy and impact (performance) objectives? | `impactmgmt_reviewstrategy` | `impactmgmt_reviewstrategy_rating` (1) |
| Are the impact objectives part of the business performance evaluation? | `impactmgmt_evaluation` | `impactmgmt_evaluation_rating` (1) |
| How do you measure / monitor your impact? | `impactmgmt_measuremonitor` | `impactmgmt_measuremonitor_rating` (1) |
### How much impact  — `howmuchimpact_rating_percent`
#### Who benefits  — `whobenefits_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| If different from customers: What is the total number of people benefiting from your product(s) and/or service(s) | `impact_peoplebenefiting` | `impact_peoplebenefiting_rating` (1) |
| What percentage of your customers / beneficiaries are female? | `impact_femalebenficiaries` | `impact_femalebenficiaries_rating` (1) |
| What percentage of your beneficiaries are from vulnerable groups (for example BoP, people from rural communities, people with disabilities, children, the elderly, refugees, etc)? | `impact_vulnerablebeneficiaries` | `impact_vulnerablebeneficiaries_rating` (1) |
#### Societal impact  — `societalimpact_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| What is the core impact focus of your business? | `Impact_Branching` | n/r |
| SDG 4: Total number of people [#] that acquired knowledge and skills needed to promote sustainable development through your business to date | `Impact_SDG4` | `redit_impact_sdg4_rating` (1) |
| SDG 5: Total number of women [#] in management positions in your business | `Impact_SDG5` | `redit_impact_sdg5_rating` (1) |
| SDG 5: Total number of women [#] in workforce (full-time equivalent), employed at equal pay in your business | `Impact_SDG5_FTE` | `redit_impact_sdg5_fte_rating` (1) |
| SDG 8: Total number of jobs [#] created (full-time equivalent) through your business | `Impact_SDG8` | `redit_impact_sdg8_rating` (1) |
| SDG 8: Total number of jobs [#] created (full-time equivalent) in low-income areas, among disadvantaged groups, incl. minorities, refugees through your business | `Impact_SDG8_FTE` | `redit_impact_sdg8_fte_rating` (1) |
| SDG 8: Total number of additional people [#] that generate income through your business without a proper employment | `Impact_SDG8_Income` | `redit_impact_sdg8_income_rating` (1) |
#### Core impact: WASH  — `coreimpactwash_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| SDG 6.1: How many people received NEW ACCESS to safe and affordable drinking water to date due to your business? | `Impact_SDG6.1` | `impact_sdg61_rating` (1) |
| SDG 6.1: How many people received IMPROVED OR MORE AFFORDABLE access to safe and affordable drinking water to date due to your business? | `Impact_SDG6.1ImprovedAccess` | `impact_sdg61improvedaccess_rating` (1) |
| SDG 6.2: How many people received NEW ACCESS to adequate and equitable sanitation and hygiene to date through your business? | `Impact_SDG6.2` | `impact_sdg62_rating` (1) |
| SDG 6.2: How many people received IMPROVED OR MORE AFFORDABLE access to adequate and equitable sanitation and hygiene to date through your business? | `Impact_SDG6.2ImprovedAccess` | `impact_sdg62improvedaccess_rating` (1) |
| SDG 6.3: How much wastewater (in cubic meters) has been NEWLY treated because of your business to date that would otherwise not have been treated? | `Impact_SDG6.3` | `impact_sdg63_rating` (1) |
| SDG 6.4: How much water (in cubic meters) has been saved or newly generated because of your business to date that would otherwise not have been saved / available? | `Impact_SDG6.4` | `impact_sdg64_rating` (1) |
| How many people received new access to female health and hygiene products to date through your business? | `Impact_NewAccessFemaleHealthHygiene` | `impact_newaccessfemalehealthhygiene_rating` (1) |
| How many people received improved or more affordable access to female health and hygiene products to date through your business? | `Impact_ImprovedAccessFemaleHealthHygiene` | `impact_improvedaccessfemalehealthhygiene_rating` (1) |
#### Core impact: Waste & Sustainable agriculture  — `coreimpactwaste_sustainable_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| SDG 2: Total quantity [tonnes] of food produced through your business to date | `Impact_SDG2` | `impact_sdg2_rating` (0.3) |
| SDG 7: Total number of people [#] (e.g. farmers, producers, etc.) using water- or energy-efficient innovations or solutions thanks to your business | `Impact_SDG7` | `impact_sdg7_rating` (1) |
| SDG 11: How much ORGANIC waste (in tons) has been newly treated because of your business to date that would otherwise not have been treated? | `Impact_SDG11` | `impact_sdg11_rating` (1) |
| SDG 11: How much INORGANIC waste (in tons) has been newly treated because of your business to date that would otherwise not have been treated? | `Impact_SDG11Inorganic` | `impact_sdg11inorganic_rating` (1) |
| SDG 12: Total mass of avoided resource waste [tonnes] through prevention, reduction, recycling and reuse through your business to date | `Impact_SDG12` | `impact_sdg12_rating` (1) |
#### Climate impact  — `climateimpact_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| SDG 13: Total mass of avoided greenhouse gas emissions [tonnes] through your business to date | `Impact_SDG13` | `impact_sdg13_rating` (1) |
### Impact risk  — `impactrisk_rating_percent`
#### Impact reliability  — `impactreliability_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| Based on your data collection methods, how likely is it that your business has difficulties compiling reliable, high quality impact data? | `impactreliability_qualityimpactdata` | `impactreliability_qualityimpactdata_rating` (1) |
| Considering your efforts to engage and consult beneficiaries and partners, how likely is it that your business misunderstands or not sufficiently considers their needs and expectations? | `impactreliability_needsexpectations` | `impactreliability_needsexpectations_rating` (1) |
#### Impact sustainability  — `impactsustainability_rating_percent`
| Question | Answer column | Score column (max) |
|---|---|---|
| How likely is it that your business may prioritize revenue generation over impact because your impact is not locked into the enterprise model? | `impactsustainability_revenueoverimpact` | `impactsustainability_revenueoverimpact_rating` (1) |
| How likely is it that external events (beyond the control of the business, e.g. elections, disasters, economic crisis, etc.) disrupt your ability to deliver the envisaged impact? | `impactsustainability_externalevents` | `impactsustainability_externalevents_rating` (1) |
| How likely is it that the positive impact the business is generating may not last or that negative impact (e.g. waste) is not mitigated? | `impactsustainability_lastingimpact` | `impactsustainability_lastingimpact_rating` (1) |
| What is the negative social or environmental impact of your business and how do you (plan to) mitigate it? | `impactsustainability_negativeimpact` | `impactsustainability_negativeimpact_rating` (1) |
