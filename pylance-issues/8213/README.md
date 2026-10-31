# Pylance process remains orphaned after VS Code quits, with MCP server still listening

Issue: https://github.com/microsoft/pylance-release/issues/8213

Issue label at investigation time: `user responded`.

This workspace prepares the **large-workspace scan followed by normal application quit**
scenario reported in the comments. It is not a reproducer of a proven root cause.
It contains only original synthetic Python files and standard-library tooling; it
does not copy, enumerate, or open a user's home directory.

## Reporter context

The initial report describes an intermittent Pylance process surviving macOS Cmd+Q
with its `--clientProcessId` process gone, `PPID=1`, approximately 3.5–3.8 GB RSS,
and a localhost MCP listening socket. The reported environment is macOS 27.0
(26A428), Apple Silicon, VS Code 1.138.0, Electron 42.10.0, and Pylance 2026.3.1.

The later, more reliable partial scenario is:

- Open a large workspace, particularly the home directory.
- Quit with Cmd+Q **while Pylance is still scanning/indexing**, not after it settles.
- Observe the client exit while Pylance continues at approximately 100% CPU,
  grows to approximately 4 GB RSS, and eventually exits roughly a minute later.
- A reporter process sample showed filesystem operations including `scandir`,
  `readdir`, `lstat`, `stat`, and `access`.

Relevant public comments:

- Capture procedure and prior Windows limitation:
  https://github.com/microsoft/pylance-release/issues/8213#issuecomment-5722648576
- Reporter delayed-exit reproduction and process table:
  https://github.com/microsoft/pylance-release/issues/8213#issuecomment-5728114654
- Maintainer report of approximately 35 seconds of continued scanning on macOS:
  https://github.com/microsoft/pylance-release/issues/8213#issuecomment-5734419821

## Files

- `scenarios/issue_8213.py`: executable deterministic scan-tree generator and checker.
- `scan_tree/`: originally a small materialized seed, **not** a large-workspace
  test by itself. The 2026-10-30 Windows verification expanded this working copy
  to 65,536 modules; the setup commands below remain the reproducible preparation.
- `main.py`: a real Python entrypoint that imports one generated module and activates
  the Python language service when opened in VS Code.
- `scenarios/capture_macos.py`: a read-only macOS process/socket observer. It records
  the selected Pylance and client identities and takes one process sample after the
  client disappears. It never quits VS Code, kills a process, or connects to MCP.

There are no third-party dependencies, pinned package claims, or prescribed
`python.analysis.*` overrides: the reporter did not provide exact settings.
Record effective settings, experiments, selected interpreter, and extension version
for every product run. Python 3.10+ suffices for the setup and capture scripts.

## Reproduction steps

1. Use a disposable workspace and close/save unrelated VS Code work before any
   full-application quit. Do **not** open your real home directory for this fixture.
2. From this directory, expand the materialized seed before opening VS Code:

   ```sh
   python3 scenarios/issue_8213.py --groups 256 --modules-per-group 128
   python3 scenarios/issue_8213.py --check
   ```

   On Windows use the selected real Python interpreter instead of an unavailable
   `python3` alias. This creates 32,768 small Python modules across nested group and
   batch directories, plus package initializers. It increases filesystem traversal
   work without third-party source, symlinks, network access, or artificial sleeps.
   The scale is a test parameter, not the reporter's measured corpus size.
3. Open **this directory** as the VS Code folder, trust this synthetic workspace
   if prompted, and open `main.py`. Select a working Python interpreter. Verify
   Pylance is active. For automated UI checks use an isolated, unattended headless
   VS Code session, with actual workbench dimensions at least 1920x1080.
4. Record the Python Language Server output and evidence that scanning/indexing is
   actually in progress. Do not equate opening `main.py`, high CPU alone, or a
   completed scan with the required trigger. If the scan finishes too quickly,
   close VS Code, expand to `--groups 512 --modules-per-group 128`, reopen, and
   report this changed scale. Do not force unrelated analysis settings to invent
   a failure.
5. On macOS, identify the current Pylance `server.bundle.js` PID and the numeric
   value of **that process's** `--clientProcessId` argument. In a separate Terminal,
   start capture with those actual values:

   ```sh
   python3 scenarios/capture_macos.py --pylance-pid CURRENT_PYLANCE_PID --client-pid CURRENT_CLIENT_PID --output "$TMPDIR/issue-8213-capture-$(date -u +%Y%m%dT%H%M%SZ)"
   ```

   Replace both uppercase PID placeholders with positive integers. Do not reuse
   the example PIDs from the issue. The helper prints its initial state and then
   asks you to quit. Keep this Terminal separate from the VS Code application.
6. **While the scan is still active, quit the whole VS Code application with
   Cmd+Q.** Do not substitute closing an editor, closing only a window when others
   remain, language-server restart, direct server disposal, forced termination,
   or the Playwright runner's cleanup.
7. Retain the capture after application quit. It records UTC timestamps, process
   start times, PPID, CPU, RSS, command arguments, and Pylance-owned listening TCP
   sockets. When the referenced client is absent and Pylance remains, it requests
   a ten-second macOS sample once. Record the quit time and correlate the captured
   start times to rule out PID reuse. Capture failure is not proof of process exit.
   A zombie process is not proof of an actively scanning survivor.
8. Expected: Pylance stops with the exiting client and leaves no owned MCP listener.
   Report actual elapsed time, ongoing CPU/RSS progression, scan evidence, and
   whether the listener belongs to the **same** surviving Pylance identity.
   The helper's default 120-second observation budget is not a definition of
   "permanent"; a process still alive at the end remains inconclusive.
9. A Windows run may execute the same synthetic load and normal full-application
   quit using its documented UI command. Capture equivalent process identities and
   socket ownership externally. Label it **Windows partial coverage**. It cannot
   validate macOS Cmd+Q, POSIX orphaning, or the reporter's exact workspace.

## Evidence and limitations

- In this investigation the issue body and all four comments were fetched live.
  The reporter and maintainer process observations above are attributed public
  reports, **not fresh product observations from this workspace**.
- The fixture generator/checker was exercised locally on Windows, including
  expansion from the seed to the default 32,768-module shape in an isolated
  validation directory. This validates fixture construction, not Pylance shutdown.
- The original preparation did not run VS Code. A real Windows VS Code
  verification was subsequently executed on 2026-10-30; see the observed results
  below. It retained screenshots, process-identity timelines and socket ownership,
  but did not obtain a qualifying quit-during-active-scan observation.
- The original seed contained only 16 modules. This working copy was expanded
  during verification, first to 32,768 and then to 65,536 modules. Large-tree
  setup remains mandatory for a fresh seed; generator success is not a product
  shutdown result.
- A synthetic tree models the reported large-directory scanning trigger but does
  not preserve the reporter's home-directory topology, file mix, filesystem
  performance, exact settings, or experiment state. No dependency versions were
  reported. A passing run with this reduction cannot rule out the original report.
- macOS delayed shutdown and the permanent-orphan/MCP variant are **not confirmed
  by this prepared workspace**. The permanent case's trigger, duration, and
  relationship to delayed scanning remain unproven. A listening socket alone
  does not establish that MCP remains responsive.
- Programmatic disposal, a helper lifecycle test, or a successful Windows quit
  does not prove that the macOS reporter journey works. Do not automatically
  close the issue on such results.
- Keep raw captures outside this publishable workspace. They can contain private
  paths or arguments. Review and sanitize them before sharing, preserving the
  PIDs, timestamps, start times, and socket ownership needed for correlation.

## Observed Windows verification — 2026-10-30

**Overall outcome: INCONCLUSIVE. Do not close the issue from this attempt.**

- Product: native headless VS Code 1.143.1 on Windows; requested latest
  Marketplace prerelease, and live `getPylanceVersion` returned active Pylance
  **2026.4.101**, with prerelease identity/channel both true. This is the build
  supplied by the configured organization-managed Marketplace, not local
  development output. Python extension 2026.10.0 and Jupyter 2025.9.1 activated.
- Actual renderer dimensions were **1920 × 1080** on every launch and after
  opening the target workspace. The standard-library fixture used existing
  Python 3.14.6. No third-party packages or `python.analysis.*` overrides were
  installed or added. The separate Python Environments picker initially showed
  3.15.0 despite the Python API setup selecting 3.14.6; it was corrected and its
  full executable path verified before subsequent attempts.
- Both requested generator/checker runs succeeded. The 256 × 128 tree validated
  35,073 generated Python files; the documented larger 512 × 128 retry validated
  70,145. Pylance enumerated 35,076 and 70,148 workspace source files respectively,
  including the three existing entry/helper Python files.
- The first UI screenshot captured index startup and `scanned(3) 45 files`.
  Later timing showed index completion before normal quit. Subsequent larger-tree
  attempts captured workspace discovery and the rendered slow-enumeration
  warning, but their saved logs also show enumeration completion before quit.
  The warning alone is therefore **not proof that scanning was still active**.
- In the focused retry, an output-text wait did not match because rendered text
  used non-breaking spaces. It returned the slow-enumeration warning after its
  30-second budget. The retained screenshot shows that warning's explanatory
  text; the log timestamps invalidate it as proof of the required active trigger.
  No product failure or passing quit-during-scan verdict is inferred.
- Normal whole-application `workbench.action.quit` was dispatched through the
  real VS Code Playwright bridge, once per attempt. No forced termination,
  language-server disposal or runner cleanup was substituted for the test action.
  Session cleanup was performed only after natural exit had been observed.
- Larger-tree attempt: application PID 46908; Pylance PID 52280 created at
  22:40:33.158064 UTC; `--clientProcessId=46048`; Pylance-owned listener
  `127.0.0.1:63909`. The recorded identities were all absent at the first
  post-quit sample, 22:40:49.675694 UTC.
- Focused retry: application PID 42536; Pylance PID 30916 created at
  22:44:29.279659 UTC; `--clientProcessId=40092`; Pylance-owned listener
  `127.0.0.1:49561`. Pylance working set grew from approximately 172 MB to
  547 MB **while the client was still alive**. No sampled client-gone/server-alive
  state occurred; all three recorded identities were absent at
  22:45:28 UTC. Read-only CIM/socket observations sampled approximately
  every 3–4 seconds including query overhead; they do not establish subsecond
  exit ordering or exclude a shorter-lived survivor. No MCP request was sent.
- The Windows ordinary-shutdown observations are useful partial material only.
  **No macOS host was available**, so Cmd+Q, POSIX reparenting to PID 1, the
  reported macOS delayed shutdown and the intermittent permanent-orphan variant
  remain unverified. The synthetic tree is not the reporter's home-directory
  layout or settings. No closure recommendation is supported.

Durable artifacts are in
`C:\dd\pyrx-monitor\.generated\issueSweeper\evidence\8213\attempts\issue-monitor-2026-09-18T18-27-08-00-00-86620f24-0b7e-4b6a-98c4-069815ab668d-dc383d7a162844fe913e835a4c0d8862\8213`:
`verification-notes.md`, `verification-result.md`, `build-identity.json`,
current-run Playwright PNGs, both Windows timelines, and three server logs.
Raw local process captures contain local paths; sanitize them before publishing.

Next action: obtain a macOS run that confirms scanning is active at Cmd+Q and
correlates the same server/client identities after quit. Retain the original
partial repro and these Windows limitations; do not claim fixed or not reproduced.
