# Inlay hint variable types change the more you scroll and hover

Issue: https://github.com/microsoft/pylance-release/issues/8259

Reporter: bschnurr. Filed: 2026-10-09. Labels: none. Comments: none when checked.

Public source: https://github.com/Extrality/AirfRANS

Pinned reference: https://github.com/Extrality/AirfRANS/commit/6acde648d5a9d81a3a90366abb6c04b7b02fe2a8

The reporter opens `dataset.py`, enables Pylance variable-type inlay hints,
scrolls, and hovers over `surf_target` and its assignment. Two screenshots show
inlay hints changing from `Any` element types to `float64` element types without
describing a source edit. No hover tooltip is visible. The screenshots do not
establish that hover, rather than analysis settling, caused the change.

## Files and provenance

- `dataset.py`: complete, unmodified public AirfRANS file from the pinned
  reference. This is the **primary editor verification surface**.
- `reorganize.py`: complete, unmodified local dependency of `dataset.py`.
- `scenarios/issue_8259.py`: executable NumPy-only partial reduction. It retains
  the exact `cell_sampling_1d` implementation and the four relevant assignments
  from `Dataset`. The wrapper and numeric smoke inputs are investigation
  additions. This reduction is not known to preserve the reported failure.
- `requirements.txt`: candidate direct dependencies for opening and importing
  the primary source. These are assumptions, not reporter-provided versions.
- `requirements-numpy.txt`: smaller dependency set for the partial reduction.
- `.vscode/settings.json`: only the reported variable-type hint setting is
  enabled. No save actions, type-checking mode, analysis mode, or evaluator
  feature flags are invented.
- `provenance.json`: immutable upstream reference, original Git blob identities,
  downloaded file hashes, reduction source lines, and candidate dependency pins.
- `references/AirfRANS-README.md` and `LICENSE-AirfRANS.txt`: original upstream
  requirements, attribution, and license. No simulation data is included.

This is a two-module extraction, not a clone of the entire project. Public
sources and source comments are retained as-is; surrounding modules, training,
and CFD data are not needed to open `dataset.py`, but their absence is a fidelity
limit if a later verifier finds that broader project context matters.

## Environment

The reporter does not supply Python, NumPy, PyVista, Pylance, VS Code, extension,
or repository versions. The upstream README lists Python 3.9.12, PyTorch 1.11.0
with CUDA 11.3, PyTorch Geometric 2.0.4, and PyVista 0.36.1; these are the
project's historical training requirements, not established reporter versions.

The candidate environment uses Python 3.12 and these stable releases, all
available before the report was filed: NumPy 2.5.3, PyVista 0.49.0, PyTorch
2.14.1, PyTorch Geometric 2.8.0, and tqdm 4.70.1. Exact reporter compatibility is
unconfirmed. In particular, different NumPy typing releases can change hint
text independently of this issue.

For an issue-local environment, from this workspace:

```powershell
uv venv --python 3.12 .venv
uv pip install --python .venv/Scripts/python.exe -r requirements.txt
.\.venv\Scripts\python.exe -B -c "import numpy, pyvista, torch, torch_geometric, tqdm; import dataset; print(numpy.__version__, pyvista.__version__, torch.__version__, torch_geometric.__version__, tqdm.__version__)"
.\.venv\Scripts\python.exe -B scenarios/issue_8259.py
```

Use the corresponding `.venv/bin/python` path on Unix. Do not run training or
download the CFD dataset for this editor-only scenario.

For a reduced-input smoke check only, install `requirements-numpy.txt` instead.
That check does **not** make unresolved PyVista or Torch imports in the primary
source acceptable for an issue-level non-reproduction conclusion.

## Reproduction steps

1. Open **this directory** as the VS Code workspace. Select the intended
   interpreter explicitly and verify that NumPy, PyVista, Torch,
   `torch_geometric`, and tqdm import in that exact interpreter.
2. Record the loaded VS Code, Python extension, and Pylance versions and the
   interpreter path. Confirm `.vscode/settings.json` enables
   `python.analysis.inlayHints.variableTypes`. Do not add a save-triggered action:
   none was reported. Ensure editor inlay hints are visible if a user-level
   setting suppresses them, recording any such override.
3. Open `dataset.py`. Navigate to the `Dataset` sampling branch containing
   `surf_sampled_points = cell_sampling_1d(line_points, surf_attr)` followed by
   `surf_pos`, `surf_init`, and `surf_target`. Preserve the unchanged document.
4. Capture the initial displayed variable hints for all four variables and the
   current language-service readiness. Record both an initial view and a
   settled-analysis view; do not conflate ordinary startup with hover causality.
5. Scroll away and back through this part of the file. Hover over `surf_target`
   and the right-hand side `surf_sampled_points[:, 7:]`, as the reporter asks.
   Capture displayed hints and hover text before and after each action. The
   exact hover positions, scroll distance, delay, and order were not specified.
6. Compare against a no-hover/wait-only observation with the same unchanged
   source and readiness state. Determine whether hints remain consistent after
   analysis settles and whether any change is specifically associated with
   scroll or hover.
7. If useful for isolation, repeat in `scenarios/issue_8259.py`, but report that
   result separately as a partial-input observation. A pass in the reduction
   alone cannot justify closure.

Expected: hints and hover information stay consistent for unchanged code after
analysis settles. The reporter's screenshots show `surf_sampled_points`
changing from `NDArray[Any] | Any` to `NDArray[float64] | Any` and `surf_target`
from `ndarray[_AnyShape, dtype[Any]] | Any` to
`ndarray[_AnyShape, dtype[float64]] | Any`. The later screenshot also shows
`float64` for the surface slices; a selective stale `surf_pos` is **not**
established by these images.

The gray `line_attr=` and `cell_attr=` text in the screenshots may be argument
name inlay hints; the pinned public source uses positional arguments. Do not
transcribe displayed type hints into source annotations or silently change the
call to a keyword argument.

## Evidence and limitations

Public screenshot evidence:

- https://github.com/user-attachments/assets/e1dfe561-d236-4859-8856-8a023f198795
- https://github.com/user-attachments/assets/600f4bc4-3413-475a-bc7c-b586ce1e55ec

Both images were inspected directly. They show before/after hint types, but no
hover tooltip, timing trace, source-change history, or loaded product version.
The relevant public call chain and exact helper are preserved in `dataset.py`
and the executable partial scenario. `provenance.json` identifies the public
source and documents all fixture reductions.

Prepared trigger: opening `dataset.py` with variable hints enabled, scrolling,
and hovering over `surf_target` and its assignment. The initial investigation
did not execute the UI trigger. A downstream real-editor attempt is recorded
under **Observed results** below; it does not establish a bug or fix.

Non-UI validation completed on Windows with Python 3.12.13 and the candidate
package versions listed above:

- All four downloaded source/reference files match their original Git blob
  identities and recorded SHA-256 hashes.
- `dataset.py`, `reorganize.py`, and `scenarios/issue_8259.py` parse successfully.
- NumPy, PyVista, Torch, `torch_geometric`, tqdm, and the primary `dataset`
  module all import successfully in the same isolated interpreter.
- Running the executable partial scenario succeeds with:

  ```text
  surf_sampled_points: shape=(4, 11), dtype=float64
  surf_pos: shape=(4, 2), dtype=float64
  surf_init: shape=(4, 7), dtype=float64
  surf_target: shape=(4, 4), dtype=float64
  ```

- At the investigation stage no UI verifier, Pylance language-info query, or
  debugger had run. The later editor verification is recorded separately below.

Numerical array values and runtime dtypes do not establish Pylance's inferred
types, request ordering, cache state, or inlay rendering behavior.

Unconfirmed reporter ingredients: exact product and dependency versions,
interpreter, full checkout state, global settings, initial analysis readiness,
scroll trajectory, hover coordinates/order, and whether waiting alone produces
the same refinement. Obtain those details if the primary candidate attempt
does not reproduce. Do not auto-close based on a partial or mismatched attempt.

## Observed results

Real VS Code attempt on 2026-10-27, run
`20261027T093130680Z-43c552e7-11ba-48b7-a1ff-aa7d66def66c`:
**inconclusive**, not a closure recommendation.

- Launched this workspace headless with the unpinned latest Marketplace
  prerelease selector; the configured gallery supplied **Pylance 2026.4.101**.
  Active prerelease identity was read from the running editor bridge.
  Python extension 2026.10.0; VS Code application metadata 1.143.1.
- Selected and verified the exact existing interpreter
  `C:\dd\pyrx1\.generated\issueSweeper\evidence\8259\.venv\Scripts\python.exe`
  (Python 3.12.13), both in startup readiness and the live status bar.
  Variable-type hints enabled; live diagnostics source Pylance, default
  server mode, type checking off. The language client was running and two
  exact-file diagnostic observations were empty. A package refresh remained
  pending; this is not an assertion of a universal analysis-complete state.
- Used the unchanged primary `dataset.py`, not the synthetic reduction.
  Compared first readable hints, a wait-only control, two PageUp/two PageDown
  scroll-away/back actions, editor hovers over the LHS and RHS of line 149,
  and a pointer hover over the visible hint.
- All four rendered labels remained identical at the observation points:
  `surf_sampled_points: NDArray | ndarray[_AnyShape, dtype[flo...`;
  the three surface slices showed
  `ndarray[_AnyShape, dtype] | ndarray[_A...`.
  These literal ellipses are renderer truncation; no hidden suffix was inferred.
- Captured real hover tooltips:
  `(variable) surf_target: ndarray[_AnyShape, dtype[float64]]` and
  `(variable) surf_sampled_points: NDArray[float64]`.
  Their presence did not change the sampled rendered labels.
- Live editor range text and final disk hash confirmed the primary source
  remained unchanged. No hint was accepted. No runtime dtypes were used as
  Pylance evidence. The owned test session was stopped successfully.

The reporter's exact before/after type strings were not recreated. Unknown
reporter versions, candidate dependency choices, two-module project extraction,
truncated labels and a first capture after startup preparation prevent a
faithful issue-level non-reproduction conclusion. Obtain the reporter's full
environment and timing before deciding closure.

Evidence and detailed ordered observations are retained at:

`C:\dd\pyrx1\.generated\issueSweeper\evidence\8259\attempts\issue-monitor-2026-10-09T17-14-20-00-00-dbf651b8-b02f-4c9c-9f47-aa86bbbd2d77-e1748689d0294136aaea345ab9853ed2\8259\ui-observations.md`

All screenshots in that report were saved by this run's Playwright tool into
that exact directory. Workspace files and the reusable environment were retained.
