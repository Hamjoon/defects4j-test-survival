# Part 1 handover A

Steps 1–6 completed. Stop for Gary’s confirmation before Step 7.

## Environment

| Component | Version / status |
|---|---|
| Branch | experiment/2026-10-week1-d4j-replication |
| Defects4J | v3.0.1, commit 6d54320e0db5a357f9ab38a8e4d2e5aead7e1c09 |
| JDK | OpenJDK 11.0.32.1, aarch64 |
| Python | 3.10.12 |
| tiktoken | 0.14.0, cl100k_base |
| javalang | 0.13.0 |
| Evaluation tools | JUnit 4.13.2; Hamcrest core 1.3; JaCoCo 0.8.8 |
| Docker | Existing image reused; Compose memory limit 12 GB |
| API key | Present; confirmed inside container; value never displayed or saved |

Existing Docker configuration passed the required Defects4J, Java and Python checks. JsonRunner compiled. JUnit reported version 4.13.2 and the JaCoCo CLI help command succeeded. Download URLs and SHA-256s are in tools/VERSIONS.md. Docker Desktop’s global memory setting was not inspected; the service limit is 12 GB.

## Step 1: bundle

All seven requested copied files/directories are identical to the original bundle (recursive diff). Dataset contains 477 records, including 14 Lang records and 9 distinct classes. Existing ORIGIN.md matches the required provenance. The original bundle was not modified. See results/part1-bundle-check.json.

## Step 4: buggy Lang checkouts

| Checkout | Class | Reused | Compile seconds | Compiled | classes.modified match | Normalized source |
|---|---|---|---:|---|---|---|
| Lang-4b | LookupTranslator | True | 0.65 | True | True | equal |
| Lang-5b | LocaleUtils | False | 4.889 | True | True | equal |
| Lang-6b | CharSequenceTranslator | False | 7.439 | True | True | equal |
| Lang-11b | RandomStringUtils | False | 7.526 | True | True | equal |
| Lang-12b | RandomStringUtils | False | 4.476 | True | True | equal |
| Lang-13b | SerializationUtils | False | 4.73 | True | True | equal |
| Lang-17b | CharSequenceTranslator | False | 6.166 | True | True | equal |
| Lang-19b | NumericEntityUnescaper | False | 4.766 | True | True | equal |
| Lang-28b | NumericEntityUnescaper | False | 5.814 | True | True | equal |
| Lang-43b | ExtendedMessageFormat | False | 4.176 | True | True | equal |
| Lang-54b | LocaleUtils | False | 6.915 | True | True | equal |
| Lang-55b | StopWatch | False | 3.857 | True | True | equal |
| Lang-57b | LocaleUtils | False | 8.428 | True | True | equal |
| Lang-64b | ValuedEnum | False | 3.491 | True | True | 4 changed diff lines; comments only |

All 14 compile. Lang-4b was reused after checking checkout identity and modified classes; the other 13 were checked out as buggy versions. Lang-64b differs in two Javadoc lines: “subclassd” → “subclassed” and “subclasss” → “subclasses”. This yields four removed/added lines in the unified diff. The complete sequences of Java token types and values are identical after the required normalization, confirming comment-only changes. All other normalized sources are equal. Source paths, packages, exports and timing are recorded in results/lang-records.json; raw command logs and diffs are in results/part1-d4j-logs/.

## Step 5: prompts and tokens

Six strings were extracted by AST from the five Mistral scripts without executing them or reading the bundle’s prompt text files. Templates were written as UTF-8 bytes without an added newline. Single-pass split-and-join substitution rendered 477 × 5 = 2,385 distinct files; inserted Java code is never processed a second time.

| Technique | Rendered | Exact token matches | Nonexact | Difference range | Maximum tokens | Above 4,096 |
|---|---:|---:|---:|---|---:|---:|
| ZSL | 477 | 428 | 49 | 0..8 | 3700 | 0 |
| FSL | 477 | 428 | 49 | 0..8 | 4091 | 0 |
| CoT | 477 | 428 | 49 | 0..8 | 3807 | 0 |
| ToT | 477 | 428 | 49 | 0..8 | 3762 | 0 |
| GToT | 477 | N/A | N/A | N/A | 3889 | 0 |

All four checked techniques match the pre-check: 428 exact and 49 positive differences of +1..+8. Every record has the same difference across ZSL/FSL/CoT/ToT. No negative difference, cross-technique discrepancy, or token-check stop condition occurred. GToT has no author token count.

Template checks passed: ZSL contains no fewshot_example placeholder; FSL contains it exactly once and begins with the specified professional tester/examples sentence; the few-shot example starts with a newline followed by //Example Java Class:. AST extraction only accepts the three specified expressions. SHA-256s and tokenizer version are recorded in prompts/manifest.json and results/template-check.json.

## Step 6: probe

# Model choice and probe

User-authorized replacement on 2026-10-03: none of the paper's four models is callable through an API as of today, per user availability finding. OpenRouter and Mistral API no longer serve Mistral 7B or Mixtral 8x7B.

Selected model for Step 6 and all later steps: openai/gpt-oss-120b. Parameters: temperature 0.7, max_tokens 4096, one user message, no system message.

The availability finding for all four paper models was supplied by the user. Original OpenRouter model-list output: results/model-list.json; fresh list: results/probe-model-list.json.

Matching Mistral 7B model IDs: .

Record: Lang-28 NumericEntityUnescaper; authors ZSL tokens: 559.

HTTP status: 200; finish_reason: stop; completion tokens: 2266; provider: CoreWeave.
Start marker: True; end marker: True.
Latency: 32.516 seconds; attempt: 1.

First 10 lines:

```text
###Test START##
/*
 * Unit tests for {@link org.apache.commons.lang3.text.translate.NumericEntityUnescaper}.
 *
 * These tests are written for JUnit 4 and aim to cover all logical paths
 * inside the {@code translate} method, including normal operation,
 * hexadecimal handling, error handling and edge‑cases.
 */
package org.apache.commons.lang3.text.translate;

```

Probe artifacts are saved under runs/probe; see usage.json for reported cost.

## Unexpected findings and mechanical fixes

- Expected comment-only differences were found in Lang-64b, as detailed above.
- One Docker invocation from the repository root was denied access to the Docker socket by the command sandbox. It was rerun with the required escalation and succeeded; no experiment parameters changed.
- A temporary-script creation tool call had a JavaScript quoting error before execution. It was corrected using apply_patch; no API call or experiment output was affected.
- The existing image and author copies were reused after validation. Evaluation JARs and compiled runner bytecode remain ignored; source, version metadata, prompts, exports, and logs are committed.
- User-provided configuration now supplies container credentials through docker/.env via Compose env_file. docker/.env is gitignored; its contents were not inspected or committed. The container presence check passed.

## Resume

Await Gary’s confirmation before Step 7. No push was performed.

## Authorized model deviation

User-authorized replacement on 2026-10-03: none of the paper's four models is callable through an API as of today, per user availability finding. OpenRouter and Mistral API no longer serve Mistral 7B or Mixtral 8x7B.

Use openai/gpt-oss-120b for Step 6 and every later generation. Parameters remain temperature 0.7, max_tokens 4096, one user message and no system message. The saved model configuration is results/model-config.json. Original model-list output is preserved byte-for-byte at results/model-list.json.

The statement that none of the paper’s four models remains callable through an API is the user’s availability finding as of 2026-10-03. The saved OpenRouter list directly supports the absence of Mistral 7B. This run uses a replacement model and does not numerically replicate the paper.

Probe usage: 641 prompt tokens, 2266 completion tokens (including 999 reasoning tokens). Reported cost: $0.00040445. Request parameters were verified against the fixed protocol, assistant content was verified byte-for-byte against the raw response, and the original saved model list was verified identical to results/model-list.json.

Step 7 has not started. Stop for Gary’s review; no push was performed.
