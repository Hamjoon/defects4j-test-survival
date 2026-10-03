# Part 2 review decisions — approved after Step 3

Source: Gary's review in this conversation, 2026-10-03. These decisions amend the original Part 2 instructions. The next authorized stop is after Step 5; do not start survival runs or push at that stop.

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

Never edit generated or developer test files. Do not push. Obtain the API key only from docker/.env through compose env_file; never record it in artifacts. Stop after the Step 5 handover and commit.
