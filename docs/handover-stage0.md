# Stage 0 early-stop handover

Status: **Step 2 completed under the addendum; stopped at the Step 3 mixed/neither rule. Stage 0 remains incomplete.** Date: 2026-10-02.

All ten `classes.modified` comparisons passed, all exports succeeded, and all five buggy versions compiled. Four dataset sources match only the buggy revision after the required normalization. Cli-5 `Util` matches neither revision because of a one-character difference in a comment (`classs` in JSON versus `classes` in the checkouts). Step 3's explicit mixed/neither stop rule remains in force under the addendum, so Step 4 and the normal Step 5 completion have not been performed.

Closure-1b was checked out and removed with its active export file; Closure-4b/4f replaces it, and the original stop evidence is archived under `results/archive/stage0-initial-stop/` and commit `78edc47`.

## Repository and bundle

- Repository: `/Users/donggi/_projects/experiment-projects/llm4ts-replication`.
- Branch: `experiment/2026-10-week1-d4j-replication`.
- Imported exactly the requested author artifacts; source bundle and copied author files were not edited.
- Dataset check passed: 477 records, 16 projects, 403 distinct project/bug pairs.
- Import commit: `f4a6484`; environment commit: `15b7fe4`.
- Revised ten-checkout checks and addendum: `ae2df0d`.
- No remote configured, no push, no model calls, and no API key recorded.

## Step 1: environment passed

| Item | Recorded value |
|---|---|
| Image | `llm4ts-d4j-replication:latest` |
| Base | `ubuntu:22.04`, Ubuntu 22.04.5 LTS |
| Image manifest list | `sha256:1da9df23a6978b8f591c031de8e173c1fef23595e1e98b6f55793b06fedf3d01` |
| JDK | OpenJDK `11.0.32.1`, build `11.0.32.1+1-post-1ubuntu1-22.04-Ubuntu` |
| JAVA_HOME | `/usr/lib/jvm/java-11` |
| Defects4J | `v3.0.1` |
| Defects4J commit | `6d54320e0db5a357f9ab38a8e4d2e5aead7e1c09` |
| Python | `3.10.12` |
| tiktoken | `0.14.0` |
| javalang | `0.13.0` |
| CPU | Host `darwin/arm64`; container `aarch64` |
| Memory limit | `12884901888` bytes (12 GiB), read from cgroup |
| Lang info smoke check | Success, 61 active bugs |
| Compose project | `llm4ts-replication` |

The GitHub releases API returned no releases; the repository's newest version tag is v3.0.1. The [v3.0.1 README](https://github.com/rjust/defects4j/blob/v3.0.1/README.md) requires Java 11. The tag is pinned in the Dockerfile to preserve the version selected in this session. The requested `TZ=UTC` and Java language/encoding options are retained. The upstream README specifies `America/Los_Angeles` for tests executed outside the Defects4J framework; the Stage 0 tests used the framework.

Evidence: [environment JSON](../results/stage0-environment.json), [Python package versions](../results/stage0-python-freeze.txt), [complete successful build log](../results/stage0-docker-build.log).

## Step 2: all ten comparisons and exports passed

| Checkout | classes.modified | JSON comparison | Compile / wall time | dir.src.classes | dir.src.tests | cp.test produced |
|---|---|---|---|---|---|---|
| Lang-4b | org.apache.commons.lang3.text.translate.LookupTranslator | match | success / 2.233 s | src/main/java | src/test/java | yes |
| Lang-4f | org.apache.commons.lang3.text.translate.LookupTranslator | match | not requested / — | src/main/java | src/test/java | yes |
| Csv-1b | org.apache.commons.csv.ExtendedBufferedReader | match | success / 0.834 s | src/main/java | src/test/java | yes |
| Csv-1f | org.apache.commons.csv.ExtendedBufferedReader | match | not requested / — | src/main/java | src/test/java | yes |
| Cli-5b | org.apache.commons.cli.Util | match | success / 0.856 s | src/java | src/test | yes |
| Cli-5f | org.apache.commons.cli.Util | match | not requested / — | src/java | src/test | yes |
| Closure-4b | com.google.javascript.rhino.jstype.NamedType | match | success / 8.469 s | src | test | yes |
| Closure-4f | com.google.javascript.rhino.jstype.NamedType | match | not requested / — | src | test | yes |
| Mockito-1b | org.mockito.internal.invocation.InvocationMatcher | match | success / 25.785 s | src | test | yes |
| Mockito-1f | org.mockito.internal.invocation.InvocationMatcher | match | not requested / — | src | test | yes |

Wall times measure the full `defects4j compile` invocation, including production and test compilation; the shell's `time` output is also preserved in each log. No Closure or Mockito compile errors occurred, so there are no error tails to report. These are environment smoke timings, not benchmark measurements. Existing checkouts were reused only after validating their project/revision metadata; all ten class comparisons and exports were rerun.

Lang-4b developer tests completed successfully as a Defects4J command (exit 0), taking 28.527 s. Exactly one developer test failed: `org.apache.commons.lang3.text.translate.LookupTranslatorTest::testLang882`. This matches the exported `tests.trigger` set exactly.

Evidence: [check table](../results/stage0-d4j-checks.md), [machine-readable checks](../results/stage0-d4j-checks.json), [dataset lookup](../results/stage0-dataset-selection.json), [Lang failure report](../results/stage0-Lang-4b-failing-tests.txt), all ten raw files in `results/stage0-export/`, and full logs in `results/stage0-logs/`.

## Step 3: mixed/neither — required stop

The script ran on all five requested bugs; each has one selected dataset record. No nested/non-public class was skipped. Normalization was exactly the requested CRLF-to-LF conversion, non-ASCII removal, trailing-whitespace stripping per line, and trailing-blank-line removal. No comments or spelling differences were ignored.

| Project/bug | Class | equals_buggy | equals_fixed | buggy_equals_fixed | Diff lines vs buggy | Diff lines vs fixed |
|---|---|---|---|---|---:|---:|
| Lang-4 | LookupTranslator | True | False | False | 0 | 4 |
| Csv-1 | ExtendedBufferedReader | True | False | False | 0 | 1 |
| Cli-5 | Util | False | False | False | 1 | 4 |
| Closure-4 | NamedType | True | False | False | 0 | 2 |
| Mockito-1 | InvocationMatcher | True | False | False | 0 | 12 |

The sole normalized difference between Cli-5 JSON and the buggy checkout is line 20, inside a Javadoc comment:

```diff
- * Contains useful helper methods for classs within this package.
+ * Contains useful helper methods for classes within this package.
```

The raw versions of both lines are ASCII, so the prescribed non-ASCII-removal step cannot reconcile them. The fixed checkout contains the same `classes` spelling and additional differences. Four records establish an exact buggy-source match; Cli-5 is closest to buggy but does not meet the exact-match criterion. The overall verdict remains **mixed/neither**, and the version-check command exited 2 as intended.

Evidence: [version report and unified diff](../results/stage0-version-check.md), [per-record paths and normalized hashes](../results/stage0-version-check.json), and [raw Cli-5 comment evidence](../results/stage0-cli5-discrepancy.txt).

## Step 4: not run

| Tool | Requested version | Download / SHA-256 / smoke check |
|---|---|---|
| JUnit | 4.13.2 | not run |
| Hamcrest core | 1.3 | not run |
| JaCoCo | 0.8.8 | not run |
| TsDetect | newest release asset | not queried or downloaded |

## Mechanical issues resolved

1. Docker Desktop was initially stopped. It was started with the approved `open -a Docker` command.
2. The sandbox blocked Docker's build metadata write under `~/.docker/buildx/activity`. The build was rerun with approved escalation and succeeded.
3. Compose's default project name `docker` overlapped with unrelated existing containers. Added `name: llm4ts-replication` to isolate subsequent runs. No unrelated containers were removed or changed.
4. Defects4J publishes version tags without GitHub release objects. Used the latest tag, v3.0.1, and verified its README instead of the unavailable latest-release endpoint.
5. Added a `.dockerignore` to keep the bundle, results, tools, and working checkouts out of the image build context. They remain available through the requested `/work` bind mount.

## Open question for Gary

How should the one-character Cli-5 comment discrepancy be handled for the Step 3 criterion? The current script and report retain the strict comparison and the `mixed/neither` verdict. No bundle file, dataset source, checkout source, or normalization rule was changed to make it pass.

After Gary reviews this new stop condition, complete any authorized follow-up, then perform Step 4 and finalize the normal Step 5 handover. The separate stop before Stage 1 remains in force. No Stage 1 templates, rendering, token checks, or model probes have begun.
