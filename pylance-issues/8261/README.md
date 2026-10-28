# Variable type inlay hints are not rendered for with-item targets

- Issue: https://github.com/microsoft/pylance-release/issues/8261
- Related report: https://github.com/microsoft/pylance-release/issues/8189
- Linked public repro: https://github.com/heejaechang/pylance-repro/tree/a382a8ace1a7a65952e4187f581fc08b07b72737/pylance-issues/8261
- Classification/label supplied by live issue analysis: enhancement.

The request is a read-only variable type inlay hint (for example
`: TextIOWrapper`) after a `with open(...) as source_file` target. It is not a
request to insert an annotation: Python does not permit `as source_file:
TextIOWrapper` in this location.

## Scenarios and provenance

- `with_item_annotations_8189.py`: complete Python file retrieved from the linked
  public repro at the revision above. Its legacy comments also describe #8189
  save/code-action checks; those checks are NOT part of this #8261 investigation.
- `scenarios/issue_8261.py`: executable canonical copy of that complete file.
- `input.txt` and `audit.txt`: investigation-added text fixtures so either Python
  entry file can run from the workspace root without missing-file errors.
- `.vscode/settings.json`: the two original public settings, plus explicit
  `editor.inlayHints.enabled: "on"` as required by the public reproduction steps.
- `fixlist-manifest.json`: the scoped #8261 read-only editor checks.

The public copy already removed private comments/settings before publication;
it is not claimed to be an untouched original private reporter workspace. The
public repository's `requirements.txt` lists pydantic/pytest ranges, but this
scenario uses only builtins and imports neither package. They are intentionally
not prerequisites here.

## Reproduction steps

1. Open this folder in VS Code with the Python and Pylance extensions. Select a
   real Python interpreter and wait for Python/Pylance activation and analysis.
   The recorded original environment was Pylance 2026.4.100 and Python 3.14.6 in
   a `.venv`; its OS and VS Code version were not recorded.
   To recreate the environment, run `python3.14 -m venv .venv` (or use an
   installed Python 3.14 executable) and select that environment. No third-party
   packages are required. The local verification used exactly Python 3.14.6.
2. Confirm `python.analysis.inlayHints.variableTypes` is `true` and
   `editor.inlayHints.enabled` is `"on"`.
3. Open `with_item_annotations_8189.py` (or its canonical executable copy
   `scenarios/issue_8261.py`). Inspect line 13, the first `with open(...)`.
   The exact trigger is opening this file with variable hints enabled and
   waiting for analysis; no edit or save is required.
4. Inspect the first `source_file` target. Expected enhancement: a visible
   `: TextIOWrapper` type decoration after that name, while actual editor text
   still contains `as source_file,`. Compare the rendered line with the real
   editor text; file text alone cannot prove presence/absence of a decoration.
5. Inspect `line_count = get_value()` on line 21 as an ordinary-assignment
   variable-hint control. Check its inferred `int` type/hint independently.
   Return to line 13 and capture the unobstructed rendered editor.
6. Do NOT accept or double-click a hint, save a dirty file, invoke Fix All, or
   run an annotation code action. Those edit-producing paths are outside #8261.
7. Optional runtime fixture check, from this folder:
   `python scenarios/issue_8261.py`. It copies `input.txt` to `output.txt` and
   reads `audit.txt`. Running Python does not test editor decorations.

## Evidence and limitations

The linked public README records absent `TextIOWrapper` hints on the first
`source_file` with-target in an older verification. It explicitly states that
the public copy was not rerun and does not establish Fix All behavior. That
historical result is context, not this investigation's verdict.

Fresh headless verification on 2026-10-27 reproduced the missing hint in VS Code
1.143.1 on Windows with Marketplace prerelease Pylance 2026.4.101 and Python
3.14.6 in this workspace's `.venv`:

- The unobstructed rendered first with-target showed `as source_file,` with no
  intervening type decoration.
- A typed hover resolved `source_file` as `TextIOWrapper[_WrappedBuffer]`.
- The ordinary assignment visibly rendered `line_count: int = get_value()`,
  while the actual editor text remained `line_count = get_value()`.
- Live editor text retained the complete unannotated with statement; no edit,
  save, Fix All, code action, or hint acceptance was performed in VS Code.
- Effective variable hints were `true`, editor hints were `"on"`, and the
  interpreter and active Pylance language client were verified.

The three scoped checks yielded one reproduced missing-hint failure, one
ordinary-assignment visual-control pass, and one unchanged-source pass.
Screenshots, rendered DOM observations, runtime log, exact extension/archive
hashes, and the verifier report are retained separately in the investigation's
evidence directory, not in this portable public workspace. The owned headless
VS Code session was stopped, and launch-only interpreter settings were restored.

The executable fixture was also run successfully from the workspace root with
Python 3.14.6; `output.txt` matched `input.txt`. That checks fixture execution
only, not type-hint rendering.

The public repro exactly matches the issue's supplied action: inspect the first
with-item `source_file` for a visible type hint without altering `as
source_file,`. Missing original private settings, the reporter's unrecorded
editor/OS version, and any Python/build-version substitutions remain explicit
limitations. The current run used Pylance 2026.4.101, not the originally recorded
2026.4.100. The screenshot's narrow viewport clips the far-right end of the long
with line, but the complete first target and following comma are visible and
the full live editor text/DOM was retained. No save/Fix All or hint-acceptance
behavior is confirmed. No causal runtime trace or fix comparison is claimed.
This is a symptom reproduction, not fix acceptance. Partial verification must
not be used to close this enhancement automatically.

### Independent gated attempt

Run `20261027T191309340Z-764896b4-c746-48b9-8833-22979b6750d8` independently
opened this existing generated workspace in a fresh headless VS Code session
with Marketplace prerelease Pylance 2026.4.101 and its existing Python 3.14.6
environment. Startup readiness verified both required hint settings, the exact
interpreter, and a running Pylance client. Live language status identified
Pylance as the diagnostics source.

The unobstructed editor again displayed no type decoration between
`source_file` and its following comma, with that complete target visible.
The same frame showed the ordinary assignment's `line_count: int` decoration.
A separately captured live hover showed
`(variable) source_file: TextIOWrapper[_WrappedBuffer]`. Full live editor text
retained the original unannotated with statement and ordinary assignment.
No edit, save, Fix All, code action, or hint acceptance was performed.

This attempt saved its own Playwright screenshot receipts and report under
`.generated/issueSweeper/evidence/8261/attempts/issue-monitor-2026-10-12T20-07-17-00-00-fd8650a0-4ecb-4d41-a6d2-6349c600b009-4cabbf5ac9d843ab9eb9397a9749a5f1/8261`
in the controller checkout. The owned headless session was stopped after
evidence capture; its launch-only default-interpreter setting was removed.
The complete public original was tested; the identical canonical copy was
preserved but not separately executed. The prior limitations above still
apply, including the original Pylance-version difference, unknown reporter
editor/OS/private settings, clipped far-right line end, and absence of any
root-cause or local-fix comparison. This result is not closure guidance.
