# Part 1 handover B

Steps 7–12 completed after Gary approved the Step 6 probe. Stop at this handover. No push performed.

Model: openai/gpt-oss-120b. One generation per record and technique; no generated-test edits or normalization.

| technique | generated | MSR | CSR | syntax ok | compiles | files that run | test methods run / passed | CUT line cov (mean over compiled files) |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| ZSL | 14 | 14 | 5 | 4 | 4 | 3 | 37 / 31 | 86.12% |
| FSL | 14 | 14 | 5 | 5 | 5 | 5 | 78 / 69 | 97.42% |
| CoT | 14 | 14 | 5 | 1 | 1 | 1 | 12 / 11 | 100.00% |
| ToT | 14 | 14 | 4 | 4 | 4 | 4 | 53 / 51 | 95.98% |
| GToT | 14 | 14 | 6 | 5 | 5 | 4 | 69 / 59 | 91.17% |
| pooled | 70 | 70 | 25 | 19 | 19 | 17 | 249 / 221 | 93.23% |

Coverage is the arithmetic mean of per-file CUT line ratios over compiled files, including files whose tests fail. A missing coverage measurement yields N/A rather than dropping that file. JUnit failures are retained as results; they do not make a file a run-error when the runner produces its summary.

Method totals are observed completed results and include partial timeout runs: the 17 completed files account for 240 methods / 212 passes; the two timeout files add 9 completed methods / 9 passes. The unfinished methods are uncounted, so pooled run counts are lower bounds.


Codes: no-code = CSR unsuccessful; no-class = CSR successful without class name; syntax = parse failure; compile = javac failure; run-error = timeout/JVM/runner error; ran = runner completed (passed/total).

| Bug / class | ZSL | FSL | CoT | ToT | GToT |
|---|---|---|---|---|---|
| 4 / LookupTranslator | ran 9/10 | no-code | syntax | no-code | ran 10/10 |
| 5 / LocaleUtils | no-code | no-code | no-code | no-code | no-code |
| 6 / CharSequenceTranslator | no-code | no-code | no-code | no-code | ran 13/16 |
| 11 / RandomStringUtils | run-error | no-code | syntax | ran 20/21 | run-error |
| 12 / RandomStringUtils | no-code | no-code | no-code | no-code | no-code |
| 13 / SerializationUtils | no-code | no-code | no-code | no-code | syntax |
| 17 / CharSequenceTranslator | ran 9/10 | ran 8/12 | no-code | no-code | no-code |
| 19 / NumericEntityUnescaper | ran 9/13 | no-code | no-code | ran 11/12 | no-code |
| 28 / NumericEntityUnescaper | no-code | ran 10/11 | ran 11/12 | ran 11/11 | ran 18/21 |
| 43 / ExtendedMessageFormat | no-code | no-code | no-code | no-code | no-code |
| 54 / LocaleUtils | no-code | ran 26/26 | no-code | no-code | no-code |
| 55 / StopWatch | no-code | ran 16/19 | syntax | no-code | ran 13/17 |
| 57 / LocaleUtils | no-code | no-code | no-code | no-code | no-code |
| 64 / ValuedEnum | syntax | ran 9/10 | syntax | ran 9/9 | no-code |

## Generation and cost

70 generation calls completed using openai/gpt-oss-120b, temperature 0.7, max_tokens 4096 and one user message only. Concurrency was 2. Length finishes: 2; empty completions: 0. Parameters and all raw responses are saved under runs/lang/.
Reported generation cost: $0.06204489; probe cost: $0.00040445; total Part 1 reported API cost: $0.06244934. Missing generation cost fields: 0.

# Lang generation results

Cells: finish_reason / completion tokens; EMPTY flags empty assistant content.

| Bug / class | ZSL | FSL | CoT | ToT | GToT |
|---|---|---|---|---|---|
| 4 / LookupTranslator | stop / 2870 | stop / 2504 | stop / 1957 | stop / 3733 | stop / 1835 |
| 5 / LocaleUtils | stop / 2590 | stop / 2892 | stop / 2413 | stop / 3048 | stop / 2709 |
| 6 / CharSequenceTranslator | stop / 2543 | stop / 2838 | stop / 2545 | stop / 2450 | stop / 2640 |
| 11 / RandomStringUtils | stop / 2925 | stop / 3453 | stop / 3838 | stop / 3148 | stop / 3237 |
| 12 / RandomStringUtils | length / 4096 | stop / 3223 | stop / 3297 | stop / 3910 | stop / 3634 |
| 13 / SerializationUtils | stop / 2499 | stop / 2860 | stop / 2587 | stop / 3362 | stop / 2685 |
| 17 / CharSequenceTranslator | stop / 3060 | stop / 1936 | stop / 2582 | stop / 2640 | stop / 3158 |
| 19 / NumericEntityUnescaper | stop / 2146 | stop / 2176 | stop / 2698 | stop / 2210 | stop / 3226 |
| 28 / NumericEntityUnescaper | stop / 2370 | stop / 2032 | stop / 2383 | stop / 1998 | stop / 2692 |
| 43 / ExtendedMessageFormat | stop / 2705 | stop / 3189 | stop / 2383 | stop / 3802 | stop / 3148 |
| 54 / LocaleUtils | stop / 2760 | stop / 2303 | length / 4096 | stop / 2991 | stop / 2579 |
| 55 / StopWatch | stop / 2691 | stop / 2032 | stop / 2575 | stop / 2306 | stop / 2482 |
| 57 / LocaleUtils | stop / 3269 | stop / 2933 | stop / 3072 | stop / 3008 | stop / 2475 |
| 64 / ValuedEnum | stop / 1985 | stop / 1698 | stop / 1799 | stop / 2187 | stop / 2113 |

Generated: 70/70. Length finishes: 2. Empty content: 0. Reported cost: $0.06204489. Wall time: 1469.467 seconds.


## Compile-error categories

| Category | Error lines |
|---|---:|
| CFS | 0 |
| PDNE | 0 |
| PAI | 0 |
| IT | 0 |
| CAM | 0 |
| MAM | 0 |
| DCD | 0 |
| PCR | 0 |
| SCI | 0 |
| UE | 0 |
| VNI | 0 |
| WAP | 0 |
| AR | 0 |
| USL | 0 |
| UCL | 0 |
| other | 0 |

Total javac diagnostic error lines: 0. Full diagnostics are in generated/.../javac.err and results/compile.csv; one row per error is in results/compile-errors.csv.

## Stage wall times

| Stage | Seconds |
|---|---:|
| Step 7 generation | 1469.467 |
| Step 8 | 0.232 |
| Step 9 | 0.084 |
| Step 10 | 5.672 |
| Step 11 | 247.323 |

Step 12 report assembly wall time: 0.285 seconds (also saved in results/stage-times.json). Steps 1–6 were completed in earlier sessions; available Step 4 compile timings and Step 6 probe latency are in handover A, not reconstructed as full stage wall times.

## Authors’ historical Lang reference

| Technique | Syntax_and_import_OK True | Matching rows |
|---|---:|---:|
| ZSL | 369 | 369 |
| FSL | 612 | 612 |
| CoT | 606 | 606 |
| ToT | 706 | 706 |

Total Lang rows: 2293. Regex covers every Lang row: True. Unmatched rows: 0. Counts match the Cowork pre-check: False. This is a historical GPT-3.5-turbo reference rate only, not a comparison target. Source SHA-256: 361928543b3d9b337ba6b8668c5bdf6ec2c5642b586939b585f801aa14f0b684.

## Deviations and interpretation

- Gary authorized openai/gpt-oss-120b on 2026-10-03 because the paper’s models are unavailable through APIs. The original Mistral templates and all generation parameters were retained. This is an end-to-end pipeline study with a replacement model, not a numerical replication.
- Container credentials are supplied via ignored docker/.env; the key is still read only from OPENROUTER_API_KEY. No key was recorded in artifacts.
- The reference extraction CSV was absent from the repository copy, so it was copied unchanged from the original author bundle into bundle/extraction_outputs/. Its source/hash are recorded.
- The authors’ extraction reimplementation was used unchanged. Its CSR check is a structural proxy, not compilation; generated files are exactly its combine output. The original script is not claimed to be the recovered historical extractor.
- Step 8 class discovery uses the document’s specified regex. No package repair, import injection, method removal, formatting, or normalization was applied.
- The supplied compile/runtime classpath ordering was retained exactly. cp.test includes older project JUnit jars ahead of the pinned 4.13.2 jar; this can affect compilation/runtime and is part of the specified pipeline.
- Compiled class files are ignored; generated source, diagnostics, per-method results, JaCoCo execution data and reports are retained.
- Probe usage and completion usage include model reasoning tokens; length finishes and empty content are reported without retry or parameter changes.

## Open questions

- The reference rows are validation/filter outcomes rather than a direct modern model comparison; use them only as the document’s requested reference rates.
- Failing generated tests were run on buggy revisions. They may expose known defects or contain incorrect assertions; no correctness repair or manual oracle adjudication was performed.
- Any survival study across later versions belongs to Part 2 and needs a separate instruction.

## Run/coverage issues

```json
[
  {
    "bug_id": "11",
    "technique": "ZSL",
    "run_error": "timeout; Picked up _JAVA_OPTIONS: -Duser.language=en -Duser.country=US -Dfile.encoding=UTF-8",
    "coverage_error": ""
  },
  {
    "bug_id": "11",
    "technique": "GToT",
    "run_error": "timeout; Picked up _JAVA_OPTIONS: -Duser.language=en -Duser.country=US -Dfile.encoding=UTF-8",
    "coverage_error": ""
  }
]
```

Timeouts prevented a final JUnit summary for some files. Their reported tests_run/failed/ignored counts come from observed completed per-method events and are lower bounds; a method still running at termination is not counted. These files remain run-error, and all observed events and stderr are retained. JaCoCo coverage from the terminated JVM is retained when available. No generated test was edited or rerun.

## API routing and attempts

HTTP attempt records: 70; generation responses: 70. OpenRouter default routing was retained, with no provider overrides. Provider counts: {'DigitalOcean': 19, 'AkashML': 9, 'Crusoe': 5, 'BaseTen': 4, 'CoreWeave': 10, 'DekaLLM': 9, 'Novita': 4, 'DeepInfra': 7, 'Mancer 2': 1, 'SiliconFlow': 1, 'Together': 1}. Each response records its provider and latency; raw HTTP responses and any retry directories are retained.

A conversation interruption occurred during Step 7. The generation process continued in the background and was resumed by observing the same process; completed calls were not repeated. Generation wall time covers the uninterrupted running process.

## Reference-count discrepancy

Literal counting of every Lang row gives ZSL/FSL/CoT/ToT = 369/612/606/706, rather than the Cowork pre-check 369/306/303/353. The latter three are exactly twice the pre-check values. All 2,293 Lang rows carry Syntax_and_import_OK=True and match the requested regex. The CSV contains 980 exact distinct Lang rows, but neither exact nor logical deduplication was applied: duplicate-looking identifiers can also come from multiple buggy revisions of the same class, and this CSV has no bug-id column. The raw requested counts are retained. Continuing through Step 12 follows Gary’s explicit instruction to run without stopping; the discrepancy is a review question.

## Verification

Saved artifact verification passed for all 70 fixed-parameter requests, verbatim assistant responses and raw.java copies, and all 25 materialized files matching unchanged combine text. Source SHA-256s remained unchanged after compilation and execution. Cross-stage counts and javac diagnostics reconcile; original model-list bytes and extractor SHA-256 are preserved. The credential scan found no API key in the checked artifacts. Evidence: results/pipeline-validation.json.

The 19/70 compile result applies to this specified extraction-to-compilation pipeline. Forty-five responses had detected code but failed the unchanged structural CSR filter, and six materialized files failed parsing; their Java compilability was not independently assessed. This filter is the main loss before compilation, and should be considered when interpreting the result.
