# Stage 0 early-stop handover

Status: **Stopped during Step 2; Stage 0 is incomplete.** Date: 2026-10-02.

The instruction to compare `classes.modified` with the JSON records for every checkout cannot be satisfied for Closure-1b: Defects4J reports `com.google.javascript.jscomp.RemoveUnusedVars`, but the supplied dataset contains **zero records for Closure bug 1**. The dataset contains 68 Closure records spanning 63 bug IDs, beginning with bug 4. This is a dataset-selection contradiction, not a mechanical command failure. No replacement bug was chosen and the comparison requirement was not waived.

## Repository and bundle

- Repository: `/Users/donggi/_projects/experiment-projects/llm4ts-replication`.
- Branch: `experiment/2026-10-week1-d4j-replication`.
- Imported exactly the requested author artifacts; source bundle and copied author files were not edited.
- Dataset check passed: 477 records, 16 projects, 403 distinct project/bug pairs.
- Import commit: `f4a6484`; environment commit: `15b7fe4`.
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

The GitHub releases API returned no releases; the repository's newest version tag is v3.0.1. The [v3.0.1 README](https://github.com/rjust/defects4j/blob/v3.0.1/README.md) requires Java 11. The tag is pinned in the Dockerfile to preserve the version selected in this session. The requested `TZ=UTC` and Java language/encoding options are retained. The upstream README specifies `America/Los_Angeles` for tests executed outside the Defects4J framework; all planned Stage 0 tests use the framework.

Evidence: [environment JSON](../results/stage0-environment.json), [Python package versions](../results/stage0-python-freeze.txt), [complete successful build log](../results/stage0-docker-build.log).

## Step 2: all checkouts succeeded; exports stopped at Closure-1b

| Checkout | classes.modified | JSON comparison | Compile / wall time | dir.src.classes | dir.src.tests | cp.test produced |
|---|---|---|---|---|---|---|
| Lang-4b | org.apache.commons.lang3.text.translate.LookupTranslator | match | not run / — | src/main/java | src/test/java | yes |
| Lang-4f | org.apache.commons.lang3.text.translate.LookupTranslator | match | not requested / — | src/main/java | src/test/java | yes |
| Csv-1b | org.apache.commons.csv.ExtendedBufferedReader | match | not run / — | src/main/java | src/test/java | yes |
| Csv-1f | org.apache.commons.csv.ExtendedBufferedReader | match | not requested / — | src/main/java | src/test/java | yes |
| Cli-5b | org.apache.commons.cli.Util | match | not run / — | src/java | src/test | yes |
| Cli-5f | org.apache.commons.cli.Util | match | not requested / — | src/java | src/test | yes |
| Closure-1b | com.google.javascript.jscomp.RemoveUnusedVars | no JSON record; STOP | not run / — | not run | not run | not run |
| Mockito-1b | not exported before stop | not run | not run / — | not run | not run | not run |

The Mockito-1 dataset record exists and names `InvocationMatcher`; its `classes.modified` export has not been run. All six requested export properties, plus `classes.modified`, were saved for each Lang/Csv/Cli checkout. Closure-1b's raw export contains only `classes.modified`. No Mockito export file exists yet. No compile or developer-test command was run, so there are no Closure/Mockito compile-error tails and no Lang failing-test count.

Evidence: [check table](../results/stage0-d4j-checks.md), [machine-readable checks](../results/stage0-d4j-checks.json), [Closure raw export](../results/stage0-export/Closure-1b.txt), [dataset lookup](../results/stage0-dataset-selection.json), and `results/stage0-logs/`.

The exact stop reason was:

```text
Modified class mismatch for Closure-1b: export=['RemoveUnusedVars'], JSON=[].
```

## Step 3: not run

Buggy-versus-fixed verdict: **undetermined**. The per-record comparison table does not exist yet. `scripts/d4j_version_check.py` was prepared while Step 2 was running but has not been executed or validated against the checkouts. No claim about the source version is made.

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

## Decision needed from Gary

May Closure-1b remain a build-only smoke target with its dataset class comparison recorded as **not applicable**, since Closure-1 is absent from the dataset? This preserves the requested checkout and compile target. Alternatively, Gary can specify a dataset-backed Closure bug and authorize changing the target.

After Gary resolves this Step 2 condition, finish its exports/builds/Lang tests, then run Steps 3–4 and write the completed Stage 0 handover. Still stop at Step 5 for Gary's separate authorization before Stage 1. Stage 1 templates, rendering, token checks, and model probes have not begun.
