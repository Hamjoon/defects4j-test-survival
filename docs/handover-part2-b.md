# Part 2 handover B — Step 5 stop

Steps 4–5 are complete under the approved Step 3 review decisions. Stop here. No survival runs (Step 6 onward) or push were performed.

## Final populations

| Record / CUT | D_r (target) | D_r_own | L_r | Rounds | Reached full D_r | ZSL | FSL | CoT | ToT | GToT |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 4 / LookupTranslator | 136 | 1 | 143 | 3 | yes | 26 (18.2%) | 18 (12.6%) | 30 (21.0%) | 40 (28.0%) | 29 (20.3%) |
| 5 / LocaleUtils | 12 | 12 | 130 | 1 | yes | 21 (16.2%) | 27 (20.8%) | 28 (21.5%) | 30 (23.1%) | 24 (18.5%) |
| 6 / CharSequenceTranslator | 141 | 0 (N/A survival) | 181 | 4 | yes | 27 (14.9%) | 24 (13.3%) | 45 (24.9%) | 33 (18.2%) | 52 (28.7%) |
| 11 / RandomStringUtils | 10 | 10 | 104 | 1 | yes | 14 (13.5%) | 26 (25.0%) | 21 (20.2%) | 20 (19.2%) | 23 (22.1%) |
| 12 / RandomStringUtils | 8 | 8 | 87 | 1 | yes | 0 (0.0%) | 18 (20.7%) | 16 (18.4%) | 31 (35.6%) | 22 (25.3%) |
| 13 / SerializationUtils | 207 | 23 | 240 | 5 | yes | 46 (19.2%) | 33 (13.8%) | 45 (18.8%) | 46 (19.2%) | 70 (29.2%) |
| 17 / CharSequenceTranslator | 44 | 0 (N/A survival) | 49 | 1 | yes | 9 (18.4%) | 8 (16.3%) | 11 (22.4%) | 11 (22.4%) | 10 (20.4%) |
| 19 / NumericEntityUnescaper | 30 | 1 | 53 | 1 | yes | 9 (17.0%) | 13 (24.5%) | 11 (20.8%) | 11 (20.8%) | 9 (17.0%) |
| 28 / NumericEntityUnescaper | 19 | 0 (N/A survival) | 61 | 1 | yes | 11 (18.0%) | 10 (16.4%) | 11 (18.0%) | 11 (18.0%) | 18 (29.5%) |
| 43 / ExtendedMessageFormat | 6 | 6 | 38 | 1 | yes | 12 (31.6%) | 0 (0.0%) | 7 (18.4%) | 19 (50.0%) | 0 (0.0%) |
| 54 / LocaleUtils | 11 | 11 | 76 | 1 | yes | 23 (30.3%) | 26 (34.2%) | 0 (0.0%) | 0 (0.0%) | 27 (35.5%) |
| 55 / StopWatch | 5 | 5 | 66 | 1 | yes | 0 (0.0%) | 16 (24.2%) | 22 (33.3%) | 15 (22.7%) | 13 (19.7%) |
| 57 / LocaleUtils | 0 | 0 (N/A survival) | 139 | 1 | yes | 28 (20.1%) | 30 (21.6%) | 29 (20.9%) | 26 (18.7%) | 26 (18.7%) |
| 64 / ValuedEnum | 74 | 18 | 99 | 3 | yes | 21 (21.2%) | 21 (21.2%) | 17 (17.2%) | 18 (18.2%) | 22 (22.2%) |

Full developer population: 703 methods; dev-own: 95; LLM: 1466. 14/14 records meet the full developer target.

Records already meeting D_r after round 1 received no additional calls. The five techniques were all generated and evaluated before each round’s stopping decision. No source normalization, test repair, package repair or method removal was applied.

## Calls and cost

| Record | Rounds | New completions | New HTTP attempts | New reported USD | Including reused r1 USD |
|---|---:|---:|---:|---:|---:|
| Lang-4 | 3 | 10 | 10 | 0.008811359 | 0.013555926 |
| Lang-6 | 4 | 15 | 15 | 0.013638435 | 0.018424964 |
| Lang-13 | 5 | 20 | 20 | 0.017050063 | 0.020905849 |
| Lang-64 | 3 | 10 | 10 | 0.005079890 | 0.007863368 |

New completions: 55; new HTTP attempts: 55. Reused round-1 completions: 70. Total completions represented: 125.

New reported usage cost: $0.044579747. Reported cost including reused round 1: $0.106624640. Successful attempts missing cost: 0. These amounts exclude the Part 1 probe; reused calls are historical cost, not new spending.

results/p2-rounds.csv records per-record cumulative passing counts and cost after every round. cumulative_cost_usd includes that record’s reused round 1; cumulative_new_cost_usd includes only its new rounds. Global cumulative fields follow CSV ledger order: reused round-1 records in bug-id order, then completed new rounds in execution order. They describe accounting order rather than the original round-1 call timestamps. Cost uses usage.cost once per HTTP attempt, with canonical successful-response copies excluded from double-counting.

Provider counts for new completions: {'Novita': 2, 'DigitalOcean': 15, 'DeepInfra': 8, 'CoreWeave': 6, 'Mancer 2': 5, 'AkashML': 8, 'Phala': 1, 'DekaLLM': 5, 'Crusoe': 4, 'Amazon Bedrock': 1}. Default OpenRouter routing was retained.

## Timing

Step 4 recorded process wall time: 860.751 seconds. Each round has generation_seconds and evaluation_seconds in p2-rounds.csv. Concurrency was at most four API calls; source evaluation within each round was sequential.

Step 5 report construction time is recorded in results/p2-population-timing.json. Editing and offline verification time are not represented as generation wall time.

## Anomalies

- Lang-4 r3 FSL: compile failure {'other': 4}; `generated/p2/Lang-4/r3/FSL/javac.err`.
- Lang-6 r2 ZSL: unstructured extraction; no source repairs or additional call.
- Lang-6 r2 FSL: compile failure {'CFS': 5}; `generated/p2/Lang-6/r2/FSL/javac.err`.
- Lang-6 r3 FSL: compile failure {'CFS': 5}; `generated/p2/Lang-6/r3/FSL/javac.err`.
- Lang-6 r4 ToT: compile failure {'CFS': 1}; `generated/p2/Lang-6/r4/ToT/javac.err`.
- Lang-13 r2 CoT: compile failure {'IT': 1}; `generated/p2/Lang-13/r2/CoT/javac.err`.
- Lang-13 r3 ZSL: compile failure {'CFS': 1}; `generated/p2/Lang-13/r3/ZSL/javac.err`.
- Lang-13 r3 FSL: compile failure {'IT': 1}; `generated/p2/Lang-13/r3/FSL/javac.err`.
- Lang-13 r4 FSL: compile failure {'IT': 1}; `generated/p2/Lang-13/r4/FSL/javac.err`.
- Lang-13 r4 ToT: compile failure {'CFS': 1}; `generated/p2/Lang-13/r4/ToT/javac.err`.
- Lang-13 r5 ToT: compile failure {'CFS': 5}; `generated/p2/Lang-13/r5/ToT/javac.err`.
- Lang-64 r2 GToT: compile failure {'PCR': 1}; `generated/p2/Lang-64/r2/GToT/javac.err`.
- Lang-64 r3 FSL: compile failure {'SCI': 1, 'other': 1}; `generated/p2/Lang-64/r3/FSL/javac.err`.
- Lang-64 r3 ToT: compile failure {'PCR': 1}; `generated/p2/Lang-64/r3/ToT/javac.err`.

Ordinary assertion failures and exceptions remain in the per-file results and are excluded from the passing population. Round-1 anomalies remain documented in handover-part2-a.md.

## Approved reporting changes for Steps 6–8

The full D_r remains the round target. dev-own is the exact matching test class filter and needs no extra runs. D_r_own is shown above. Lang-6 and Lang-17 have no matching class. Lang-28 has a matching class but zero passing methods, so its dev-own survival is also N/A. No baseline is manufactured for these empty subsets.

Keep population = dev in p2-survival-methods.csv and add own_class as a boolean; use it to derive dev-own. All Step 8 tables that report dev must also report dev-own (time points, days, failure kinds, class-level 2x2, counts matched). The Step 5 manifest supplies all passing developer rows with this flag.

Lang-57 stays in the experiment. Developer survival is N/A at every time point with note "all developer methods are trigger tests; no developer baseline at t". LLM survival is computed normally. Exclude Lang-57 from class-level 2x2 counts and put that exclusion in a footnote; also footnote empty dev-own baselines for that subset’s 2x2.

139 LLM methods passed at the buggy version where every developer method fails.

Repeat the preceding observation in handover-part2-c without interpretation. The decisions are preserved in docs/part2-review-decisions.md and results/p2-approved-policy.json.

## Reproducibility and verification

All completed calls retain canonical request.json, raw-response.json, response.md, raw.java, usage.json and run.json, plus every attempt under attempt-N. Raw responses and test sources are immutable. The retry/resume checks used offline fixtures before any new API call. Successful call artifacts and completed evaluation artifacts are reused on restart; uncertain transport attempts stop without blind retry.

See results/p2-validation-b.json for request-parameter/prompt checks, response and source hashes, population filtering, stopping-policy checks, cost reconciliation and the credential scan. The API key was supplied only by compose env_file.

## Stop

Step 5 is the required review stop. Steps 6–9 have not begun.
