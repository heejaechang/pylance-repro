# Override completion expands a cross-module union alias without importing its members

Issue: https://github.com/microsoft/pylance-release/issues/8276

Reported title: “automatically expanded Union member types are not imported when method is auto-inserted”

## Current preparation handoff

**No UI verification has been run for this preparation attempt (2026-11-03 UTC).**
This attempt only reviewed retained evidence, checked the scenario files and
interpreter, and prepared this workspace for the next verification phase.
Repository source is read-only. No completion was accepted, no Jest repro was
run, and no new real-product or causal verdict was established.

The issue remains eligible: accepting an inherited-method completion in another
module is a concrete Pylance workflow. The return and parameter cases below are
real pre-acceptance editor inputs, not placeholders. The current execution
verdict is **blocked pending the separately requested verification phase**, not
`not_reproduced` or `fixed`. This is a scope boundary, not a tool failure.

Historical reports retained below describe an old Marketplace failure and a
local-development-build pass. They are useful leads, but their conclusions are
not inherited as this attempt's verdict. There is no complete paired-build
acceptance record establishing the intended fix, and release shipment has not
been verified.

For the next phase:

- Use `scenarios/return/` and `scenarios/parameter/` as separate VS Code folders.
- Select the intended Python interpreter in each live folder; the settings
  contain no machine-specific interpreter path.
- Retype `@override`, Enter, and `def f`; select and accept the actual `func`
  suggestion. Capture the full resulting document and settled diagnostics.
- Pass `headless: true` on every Playwright start, and verify actual
  `window.innerWidth >= 1920` and `window.innerHeight >= 1080` before UI checks.
- Record the exact product identity. Do not equate a development version, a
  label, or source inspection with successful fix verification.
- Keep screenshots, runtime logs, and provenance outside this public workspace.

Live issue checked on 2026-11-02: open, labels `bug` and `fixed in next version (main)`, no comments.

The fixed-version label indicates intended implementation status, not evidence that the fix has shipped or passed release verification.

The reporter accepts the inherited `func` override completion after typing `@override` and `def f` in a subclass in another file. The generated return annotation expands `U` to `A | B`, but neither member is imported. The reporter also names a parameter-annotation variant and prefers preserving and importing `U`.

Public reporter screenshots:

- [Completion selection after `def f`](https://github.com/user-attachments/assets/122ff923-2843-4e4f-8eef-6a2129d33e80)
- [Inserted return annotation with unresolved `A` and `B`](https://github.com/user-attachments/assets/ef41a63c-edfb-4f8f-b7f4-f4916b6f30bf)

## Files and environment

- [`scenarios/issue_8276.py`](scenarios/issue_8276.py): verbatim first Python code block from the issue, retained as the original base-class specimen. It does not trigger a completion by itself.
- [`scenarios/return/o1.py`](scenarios/return/o1.py): that same specimen under the reporter's module name, for the return-annotation case.
- [`scenarios/return/derived.py`](scenarios/return/derived.py): screenshot-equivalent subclass at the completion insertion point.
- [`scenarios/parameter/o1.py`](scenarios/parameter/o1.py): the explicitly reported `def func(self, u: U) -> None` variant.
- [`scenarios/parameter/derived.py`](scenarios/parameter/derived.py): the corresponding completion insertion point.

Reporter environment: Ubuntu 24.04.4, Python 3.14.3 installed with `uv venv`, Pylance 2026.4.101. No third-party Python packages or analysis settings were supplied.

Use Python 3.14.3 for a faithful run. For example, from this workspace root, `uv venv --python 3.14.3 .venv` prepares an environment if that interpreter can be acquired. Select the resulting interpreter in VS Code and record its actual version. The retained local `.venv` was provisioned during the earlier run and its executable was freshly checked as Python 3.14.3 for the verify attempt below. Do not export the virtual environment; recreate it on the target host.

No `requirements.txt` is supplied because the issue names no third-party packages. Each case contains `.vscode/settings.json` with `python.analysis.generateWithTypeAnnotation=true`. This is an explicit **test assumption**, not a reporter-provided setting. It exercises the annotated completion shown in the screenshots: the earlier default-settings control generated no annotations when type checking was off. No host-specific interpreter path is required in the retained public settings. Select the intended interpreter in each live workspace. Record effective settings and the exact Pylance build used for each verification run.

## Reproduction steps

Run the two cases separately. Open the **case directory itself** as the VS Code folder so each case's `from o1 import Base` resolves to its own sibling `o1.py`, not the other variant.

### Return annotation

1. Open `scenarios/return/` as the workspace folder. Select the intended Python interpreter, open `o1.py`, and confirm it contains `type U = A | B` and `def func(self) -> U: ...`.
2. Open `derived.py`. Its initial contents match the reporter's pre-acceptance screenshot:

   ```python
   from o1 import Base
   from typing import override

   class Derived(Base):
       @override
       def f
   ```

3. To replay the reporter's typing gesture, delete lines 5–6, leave the class header intact, and type the indented `@override`, press Enter, and type `def f`. The resulting caret position is **line 6, column 10**, immediately after `f`. Do not type a full signature or import `U`, `A`, or `B` yourself.
4. In the suggestion popup, explicitly select **`func`**, then **accept that completion**. Pressing Enter with `func` selected is a reproducible acceptance gesture; the reporter did not specify the acceptance key. If the popup is absent, record that before trying an explicitly requested suggestion as a separate fallback.
5. Capture the complete resulting document, including imports and the generated method, and any unresolved-name diagnostics after analysis settles.

Reporter-observed failure:

```python
from o1 import Base
from typing import override

class Derived(Base):
    @override
    def func(self) -> A | B:
        return super().func()
```

`A` and `B` are unresolved in that screenshot. The preferred expected outcome is `def func(self) -> U:` with `U` imported from `o1`, for example `from o1 import Base, U`. Import formatting or a separate `from o1 import U` is not material.

### Parameter annotation

1. Open `scenarios/parameter/` as a separate workspace folder. Its sibling `o1.py` differs only in the method declaration: `def func(self, u: U) -> None: ...`.
2. Open its `derived.py`, reset and retype lines 5–6 as above, ending at **line 6, column 10**, immediately after `f`.
3. Select **`func`** and accept the override completion through the suggestion popup.
4. Capture the resulting imports, signature, body, and unresolved-name diagnostics. The preferred expected signature is `def func(self, u: U) -> None:` with `U` imported from this case's `o1.py`. Do not manually repair the imports before observing the result.

For either case, expanding `U` to `A | B` and importing both names would satisfy the reporter's alternative expectation, but would not meet the preferred alias-preservation check.

Before repeating a case or changing builds, restore `derived.py` to its supplied pre-acceptance contents, including removal of any generated imports and method body.

## Evidence and limitations

- **Grounding:** the live issue body and both attached screenshots were inspected. `scenarios/return/derived.py` preserves their `Base`, `Derived`, `@override`, and `def f` shape. `scenarios/parameter/o1.py` applies the explicit parameter variant in the body to `Base.func`; the body calls it `U.func`, although `U` is the union alias and the supplied class is `Base`.
- **Current attempt:** issue details and screenshot descriptions were supplied by the caller's live analysis. This attempt inspected the persisted scenarios and historical reports, not a fresh issue fetch or a fresh UI session. Both scenario files remain at the incomplete `def f` trigger. No current completion output or diagnostic result has been observed.
- **Observed results:** reporter evidence and two separate local runs are distinguished below. The earlier Marketplace 2026.4.101 run recorded the reported failure; the fresh existing-local-build run preserved and imported `U` for both variants. Neither result alone verifies the release containing the merged fix.
- **Trigger:** accepting the `func` override completion is required. Add Type Annotation, import quick fixes, manually inserting expected output, and save actions are not substitutes.
- **Intentional incomplete files:** both `derived.py` files end at `def f`, just before accepting completion. They are real editor inputs, not executable scripts; syntax errors at this intermediate point are expected and do not establish the reported bug.
- **Assumptions:** each new subclass file is a sibling of its case's `o1.py`; the reporter did not specify the new filename or full folder topology. The two isolated case directories avoid mixing the return and parameter variants.
- **Unconfirmed reporter steps:** acceptance key, VS Code version, effective user/workspace settings, interpreter path, and completion resolve mode were not supplied. Enabling annotation generation is a recorded assumption, not a reconstruction of unknown reporter settings. Enter is the verifier's acceptance gesture, not a known reporter key.
- **Environment limits:** Python 3.14.3 was matched, but the UI runs used Windows rather than the reporter's Ubuntu 24.04.4. The merged fix's release availability and paired baseline/fix build provenance remain unverified. These artifacts do not support automatic closure.
- **Next verification:** use the same completion-acceptance journey for both cases and record build/interpreter identity, effective settings, full edited documents, and diagnostics. A fixed-version label is not execution evidence. Automated VS Code runs should start headless and establish an actual workbench size of at least 1920×1080 before UI checks.

## Earlier Marketplace reproduction — 2026-11-02

**Earlier recorded outcome: reproduced for both annotation variants on Marketplace 2026.4.101. This is historical evidence reviewed for relevance, not the verdict of the fresh local-build attempt below. Do not recommend closure.**

Run ID: `20261102T100717247Z-c4e78fa8-3575-4bf1-a53c-26ac9bb98274`.

The canonical Playwright runner opened each case directory separately in one owned headless VS Code session. Actual renderer size was verified as 1920×1080 before checking each folder. Requested latest Marketplace prerelease resolved to active **Pylance 2026.4.101**, not a local development build. VS Code was **1.143.1** on Windows x64, Python extension 2026.10.0, Jupyter 2025.9.1. Exact **Python 3.14.3** was provisioned with `uv venv --python 3.14.3 .venv`; no third-party dependencies were needed. The interpreter executable is `.venv\Scripts\python.exe`.

### Important setting discovered through the live UI

The first default-settings return attempt accepted the actual `func` suggestion but generated **no annotation**:

```python
    def func(self):
        return super().func()
```

This attempt is **inconclusive for the annotation/import bug**, not a successful fix verification. Live Settings describes `python.analysis.generateWithTypeAnnotation` as defaulting to false when type checking is off and true for other modes. Type checking was off. To exercise the annotated output shown by the reporter, this run explicitly enabled:

```json
{
    "python.analysis.generateWithTypeAnnotation": true
}
```

This workspace setting is retained in each case's `.vscode/settings.json` for repeatability. It is an explicit test configuration, **not an assertion about the reporter's unknown settings**. Other live settings observed were diagnostics source Pylance, diagnosticMode openFilesOnly, languageServerMode default, enableAsyncProgram false, empty severity overrides, and auto-import completions false.

### Actual accepted output and diagnostics

In each variant, the decorator and partial method were retyped through the Monaco UI; the caret was verified at line 6 column 10. The suggestion popup opened automatically. The `func` row was explicitly selected and accepted with **Enter**, without injecting provider results, adding annotations afterward, applying import fixes, or saving to trigger fixes.

Return output:

```python
from o1 import Base
from typing import override

class Derived(Base):
    @override
    def func(self) -> A | B:
        return super().func()
```

Parameter output:

```python
from o1 import Base
from typing import override

class Derived(Base):
    @override
    def func(self, u: A | B) -> None:
        return super().func(u)
```

Both showed Pylance `reportUndefinedVariable` warnings: `"A" is not defined` and `"B" is not defined`, line 6 columns 23 and 27. Two post-acceptance diagnostic observations agreed in each case, and the saved screenshots show the complete document/imports and Problems rows.

Both live documents were reverted and read back to their original insertion points after evidence capture. The owned session was stopped successfully; the workspace and `.venv` are retained.

### Evidence and remaining limits

Evidence directory:

`.generated/issueSweeper/evidence/8276/attempts/issue-monitor-2026-10-23T00-48-15-00-00-2011417c-45d5-42be-befc-6693b25c382d-bc81f04c38a8455dac6d123b80d2c940/8276/`

- `verification-report.md`: environment, default-setting control, both annotated outcomes, readiness/recovery notes, provenance, and limitations.
- `8276-return-reproduced.png` and `8276-parameter-reproduced.png`: fresh actual VS Code documents and Problems.
- `8276-return-annotated-popup.png` and `8276-parameter-popup.png`: actual suggestion lists before acceptance.
- `return-accepted.txt` and `parameter-accepted.txt`: complete live outputs transcribed after observation, normalized to LF.

This was Windows rather than the reporter's Ubuntu 24.04.4. Python and Pylance versions matched; the reporter's VS Code version, effective settings, resolve mode, and actual acceptance key remain unknown. The native Marketplace resolver selected 2026.4.101 in this environment; this is not evidence that a later/main-branch fix has shipped or been tested. No local paired-build fix verification was performed.

## Fresh existing-local-build check — 2026-11-02

Run ID: `20261102T234054009Z-f0799a7d-0d80-49c0-ba6d-c14dc49e6a48`.

**MODE=verify execution verdict: blocked for complete fix/release verification. Supplemental UI result: both cases passed the alias-preservation and import check on the existing local development build.**

The canonical Playwright runner opened each case as the sole folder, headless. The actual workbench measured **1920×1080 before both cases**. The intended Python 3.14.3 environment was selected. The loaded Pylance identified itself as **9999.0.0-dev** from the requested local extension path. Logs and process paths corroborated that path, and loaded bundle hashes matched the supplied existing bundles before and after the checks.

In each case the verifier retyped `@override`, Enter, and `def f`, explicitly selected `func` in the real suggestion widget, and accepted with **Enter**. No Add Type Annotation action, direct provider call, import repair, or manually inserted expected signature substituted for accepting completion.

Return output:

```python
from o1 import U, Base
from typing import override

class Derived(Base):
    @override
    def func(self) -> U:
        return super().func()
```

Parameter output:

```python
from o1 import U, Base
from typing import override

class Derived(Base):
    @override
    def func(self, u: U) -> None:
        return super().func(u)
```

Post-acceptance diagnostics were empty. Both unsaved completions were native-reverted and the original insertion-point fixtures were verified. The owned VS Code session was stopped.

### Limits and next verification

- `python.analysis.generateWithTypeAnnotation=true` remained an explicit test assumption; type checking was off. The reporter's effective settings remain unknown.
- Windows is not the reporter's Ubuntu host. This run checks the concrete completion journey, not Ubuntu-specific parity.
- The checkout contains the merged fix, but pre-existing build outputs have no established source-to-build attestation. A development version, merge ancestry, and matching bundle hashes do not independently establish which source produced those bundles.
- No authorized unchanged-source baseline build, task-worktree fix build, or validation `DIFF_ID` was supplied. The fresh pass is therefore **supplemental current-build evidence**, not canonical paired-build `fixed` acceptance and not empirical proof of release shipment.
- Next: replay both suggestion-acceptance cases on the exact intended release build with artifact identity. For canonical local-fix attribution, obtain separately authorized paired baseline/fix builds and the current validation `DIFF_ID`. Do not request a new fix merely because complete verification is pending.

Local-only evidence is retained outside this public workspace at repo-relative
`.generated/issueSweeper/evidence/8276/verify-20261102T234054009Z-f0799a7d-0d80-49c0-ba6d-c14dc49e6a48/`.
It includes `fixlist-result.md`, `run-notes.md`, `environment-provenance.json`,
`ui-observations.json`, complete return/parameter observed text, suggestion/accepted/restored screenshots, and runtime logs. These are investigator evidence references, not required dependencies for replaying this workspace.

For public export, retain this README, all five scenario Python files, and both case settings files. Exclude `.venv`, caches, machine-specific runtime receipts/logs, and any local Git metadata. The workspace files contain the issue's public sample, not private product implementation code.
