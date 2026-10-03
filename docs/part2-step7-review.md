# Step 7 patch-direction review — Steps 5b and 6 complete

Step 5b was committed as e53a72c. Step 6 has completed all 105 record/timepoint pairs and 12,803 method/timepoint rows. Steps 7–9 are pending the patch-direction decision; handover-part2-c.md has not been written as a completed handover. No push.

## Concrete contradiction

The original Part 2 document instructs Step 7 to obtain fixed-version lines by taking the `+` side of Defects4J patches. Its working-mode rule says: “Stop early for an error you cannot resolve, a contradiction between this document and what you find, or a result outside an expected range stated in a step.”

All 14 local source patches run from fixed to buggy. Every old-side hunk matches the fixed checkout; every new-side hunk matches the buggy checkout. The exact patches and per-file comparisons are retained under results/p2-patch-audit/.

For example, Lang-4’s patch removes `seq[0].toString()` and adds `seq[0]`. The fixed source contains the former and the buggy source contains the latter. Lang-13’s patch removes the primitiveTypes map that is present in the fixed source.

**Proposed decision:** reverse the patches for analysis, verify both reversed sides against the actual checkouts, then use changed `+` lines in the reversed patches. For deletion-only hunks, use the position line as specified. This produces fixed-version line numbers for intersection with fixed-version JaCoCo coverage. No test or production source is modified. The candidate reversal has already been verified against both versions for every record.

| Record | Original patch orientation | Old side = fixed | New side = buggy | Candidate reversal checked |
|---|---|---|---|---|
| Lang-4 | fixed-to-buggy | yes | yes | yes |
| Lang-5 | fixed-to-buggy | yes | yes | yes |
| Lang-6 | fixed-to-buggy | yes | yes | yes |
| Lang-11 | fixed-to-buggy | yes | yes | yes |
| Lang-12 | fixed-to-buggy | yes | yes | yes |
| Lang-13 | fixed-to-buggy | yes | yes | yes |
| Lang-17 | fixed-to-buggy | yes | yes | yes |
| Lang-19 | fixed-to-buggy | yes | yes | yes |
| Lang-28 | fixed-to-buggy | yes | yes | yes |
| Lang-43 | fixed-to-buggy | yes | yes | yes |
| Lang-54 | fixed-to-buggy | yes | yes | yes |
| Lang-55 | fixed-to-buggy | yes | yes | yes |
| Lang-57 | fixed-to-buggy | yes | yes | yes |
| Lang-64 | fixed-to-buggy | yes | yes | yes |

The user was asked to choose actual fixed-version lines (recommended), the literal original `+` side, or stopping after Step 5b. No response has arrived at this checkpoint. scripts/classify_fixed.py refuses to run until results/p2-approved-policy.json contains the explicit Step 7 mapping decision.

## Completed population and cost

Full developer baseline: 703 methods; dev-own: 95. LLM raw passing methods: 1,509; exact duplicates removed: 156; unique LLM population: 1,353. All 14 unique targets are met. Only Lang-13 needed an extra round after deduplication; round 6 raised it from 196 to 230 unique methods against D_r = 207.

Step 5b added five calls costing $0.004514208. The full generation ledger now contains 130 calls including 70 reused round-1 calls, with total reported generation cost $0.111138848. New Part 2 calls total 60, costing $0.049093955. No additional API calls were made for survival.

## Step 6 measurements

| Population | LLM raw at t | Duplicates removed | Frozen population | Fixed-version pass | Fixed-version fail | Fixed-version error |
|---|---:|---:|---:|---:|---:|---:|
| dev | — | — | 703 | 703 | 0 | 0 |
| dev-own | — | — | 95 | 95 | 0 | 0 |
| llm | 1509 | 156 | 1353 | 1331 | 21 | 1 |

All-timepoint statuses (method/timepoint units): {'pass': 8265, 'fail': 162, 'compile-fail': 207, 'not-run': 6, 'error': 5, 'absent': 4158}.

Step 6 performed 669 file/timepoint compilations: 9 failed and 660 proceeded to method selection/execution. Process wall time across the interrupted and resumed sessions: 464.378 seconds.

Every survival source retains its recorded SHA-256. Selected-method execution explicitly excludes duplicates and all other methods outside the frozen population. Dev-own uses the existing own_class boolean without extra runs. All 45 absent pairs are recorded without compilation or execution.

Lang-57 developer survival is N/A at every point: all developer methods are trigger tests; no developer baseline at t. It remains excluded from class-level 2×2. Its LLM population is 139 raw passes minus 35 duplicates = 104 unique methods; all 104 pass at each of its four present time points.

139 LLM methods passed at the buggy version where every developer method fails.

## Mechanical corrections and evidence

- Six initial run artifacts for Lang-13 are archived under results/archive/step6-inherited-listing/. The wrapper was corrected to assign not-run only to missing inherited methods while running remaining selected methods. Each of the three affected time points changed from 26 not-run to two not-run plus 24 passes; the 28 compile-fail methods per point were unchanged.
- The final six not-run rows are two inherited methods missing from JUnit listings at Lang-6b, Lang-5b and Lang-4b. They remain in the frozen developer denominator.
- Selection regression checks cover explicit nonpopulation exclusions, missing inherited methods, and exclusion persistence after a timeout. The complete result audit verifies every population/timepoint identity, source hash, classpath, checkout working directory, and Java launch selection.
- A host-only validation import lacked requests; validation ran in the prescribed Docker environment. A quoting error in an inline candidate-patch check was replaced with scripts/verify_selection.py. Neither failed validation command executed experiment methods or changed source files.
- Earlier baseline working-directory correction remains documented in handover-part2-a.md. No test files were edited in this continuation.

## Resume after the decision

Record the chosen mapping in docs/part2-review-decisions.md and results/p2-approved-policy.json (`step7_patch_lines`: `actual fixed-version lines` or `literal original plus side`). Then run scripts/classify_fixed.py in Docker, followed by scripts/aggregate.py. The prepared aggregator includes dev-own throughout and raw/removed/unique LLM counts. Finish the full validation and Step 9 handover with timings, costs, deviations, absent-record list, and open questions; commit without pushing.

No fixed-version classification, Step 8 final report, or completed Step 9 handover is claimed at this review checkpoint.
