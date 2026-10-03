# Stage 0 addendum (2026-10-02)

Gary directed the following after the initial Step 2 stop:

> Do not waive the comparison. Follow the addendum: drop Closure-1b, check out Closure-4b/4f and Mockito-1f, apply the Step 2 comparison to all ten checkouts, and run the Step 3 version check on five bugs (Lang-4, Csv-1, Cli-5, Closure-4, Mockito-1). Then continue through Step 5.

The revised active set is Lang-4b/4f, Csv-1b/1f, Cli-5b/5f, Closure-4b/4f, and Mockito-1b/1f. Every checkout must pass the same modified-class comparison. The five buggy checkouts receive the requested compile checks; Lang-4b receives the developer-test sanity check. No comparison is waived. Step 3 compares both revisions for all five bugs. The Stage 0 stop point at Step 5 remains in force; Stage 1 is not authorized yet.

The original stop evidence is preserved under `results/archive/stage0-initial-stop/` and in commit `7406fa1`. The obsolete Closure-1b working checkout is removed. Existing valid checkouts may be reused after checking their Defects4J project/revision metadata; their class comparisons and exports are rerun.
