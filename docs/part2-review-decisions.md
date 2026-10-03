# Part 2 review decisions — approved after Step 3

Source: Gary's review in this conversation, 2026-10-03. These decisions amend the original Part 2 instructions. The Step 5 review below authorizes continuation through the committed Step 9 handover. No push.

## Generation

The original round policy is approved: five calls per additional round, one per technique, with the existing rendered prompts, openai/gpt-oss-120b, temperature 0.7, max_tokens 4096, one user message and no system message. After each complete round, extract, compile and run at t. Stop each record when cumulative L_r(k) >= full D_r or k = 30. Round 1 is reused. Only Lang-4, Lang-6, Lang-13 and Lang-64 need additional rounds based on Step 3. HTTP errors get at most three retries, ten seconds apart, with every attempt retained. Concurrency is at most four. Record cumulative cost per round in results/p2-rounds.csv.

## Developer populations for Steps 6 and 8

The full developer population and generation target D_r are unchanged. Add a reporting subset, dev-own: methods from tests.relevant whose test class FQCN is exactly the CUT package plus <CUT simple name>Test. It is a filter over the existing dev rows and requires no extra compilation or execution. D_r_own counts the matching methods that passed at t, and is recorded in results/p2-population.md at Step 5.

Lang-6 and Lang-17 have no matching CharSequenceTranslatorTest; dev-own is empty and reported as N/A for those records.

Derived from the saved baseline: Lang-28 has a matching NumericEntityUnescaperTest, but its only method fails at t. Therefore D_r_own is also zero there, and its dev-own survival denominator is empty. Report N/A for that subset and omit its empty-subset 2x2 comparison; retain its nonempty full-dev comparison. This follows the population filter and is not a change to the round policy.

In results/p2-survival-methods.csv, keep population = dev and add a boolean own_class column. Do not duplicate rows as population = dev-own. The Step 5 population manifest supplies own_class on every passing developer method for later reuse. For LLM rows the boolean is false and is not used as a developer-subset indicator.

Every Step 8 table reporting dev must also report dev-own beside it: survival by time point, survival by days, failure kinds, class-level 2x2, and counts matched. Counts matched must continue to identify full D_r as the generation target. Empty developer subsets are N/A, not vacuous all-pass outcomes.

## Lang-57

Keep the record. D_r = 0. At every time point, report developer survival as N/A with this exact note:

> all developer methods are trigger tests; no developer baseline at t

Compute LLM survival normally. Exclude Lang-57 from class-level 2x2 counts and list the exclusion in a footnote below the table. This also applies to the dev-own comparison, whose baseline is empty.

State this observation in both handover-part2-b and handover-part2-c without further interpretation: **139 LLM methods passed at the buggy version where every developer method fails.**

## Unchanged constraints

Never edit generated or developer test files. Do not push. Obtain the API key only from docker/.env through compose env_file; never record it in artifacts. Stop after the Step 9 handover and commit.

## Step 5 review: exact duplicate methods (Step 5b)

Gary authorized Step 5b and Steps 6–9 in this conversation. This supersedes the raw-count stopping condition and the previous Step 5 stop. Commit the Step 5b artifacts, then continue to the committed Step 9 handover without pushing.

Hash every LLM test method in every structured source, including methods in files that fail compilation and methods that do not pass at t. The normalized body is the original source between the opening and closing method braces with every whitespace character removed. Names, signatures and annotations are excluded; comments and string contents remain, with whitespace removed there as well. Use SHA-256 of its UTF-8 encoding.

Deduplication is per record and among passing occurrences only. Keep the first passing occurrence by round ascending, then ZSL, FSL, CoT, ToT, GToT, then source order. A nonpassing occurrence cannot displace a later passing one. Mark later passing occurrences as duplicates and record the retained round/technique/method. Identical bodies in different records remain independent.

The Step 6 LLM population is passing methods with is_duplicate = false. Exclude duplicates from execution through runner selection; never remove them from source files. Continue complete five-call rounds only for records with L_r_unique < full D_r, stopping at the unique target or 30 total rounds. Preserve existing prompts, parameters, retry rules, concurrency and call evidence. Add cumulative_L_r_unique to every ledger row. Record raw counts, removed duplicates, unique counts, D_r, D_r_own, rounds and unique technique shares in the population report and the before/after and cost evidence in handover-part2-b-addendum.md.

Every Step 8 count of the LLM population must expose the raw passing population and the number of exact duplicates removed. Developer populations and their target remain unchanged. The historical Lang-57 observation remains 139 raw passing methods; its survival population uses the deduplicated count.

## Step 6 implementation correction

A later checkout can remove an inherited developer method from JUnit's listing even though the unchanged copied subclass still compiles. The method remains in the frozen population and receives `not-run` with `JUnitMethodMissing`; other listed population methods still run. An initial wrapper incorrectly made this a class-wide `not-run`. Six affected run artifacts (two classes at each of Lang-6b, Lang-5b and Lang-4b for the Lang-13 record) are archived under results/archive/step6-inherited-listing and were replaced by corrected measurements. This is a mechanical runner correction, not a source or population change.

## Pending Step 7 contradiction

The original document says to take fixed-version changed lines from the patch's `+` side. All 14 saved Defects4J source patches actually run from fixed to buggy: their `-` side matches the fixed checkout and their `+` side matches the buggy checkout. See results/p2-patch-audit/audit.json. The proposed correction is to reverse each patch for analysis, verify the reversed sides against both checkouts, then take the reversed `+` lines (with deletion-only hunk positions mapped as specified). The user was asked to choose this correction or literal original `+` lines. No Step 7 classification is authorized under a chosen mapping until that answer arrives; the classification script checks for the explicit decision.
