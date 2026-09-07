# Issue 8193: numpy alias completion after wildcard import

- Issue: https://github.com/microsoft/pylance-release/issues/8193
- Title: `numpy (as np) code completion breaks when put before wildcard import`
- Labels at intake: `team needs to reproduce`

The report says member completion disappears for `np` when `import numpy as np`
is followed by `from galois import *`, where `galois` also exports NumPy as
`np`. A differently named alias remains usable.

This workspace uses small local `numpy` and `galois` packages to preserve the
reported import topology without relying on third-party package versions.

## Unattended verification

1. Open `scenarios/issue_8193.py`.
2. Place the cursor after `np.` on line 4 and trigger completion.
3. The completion list should include `ndarray`.
4. As a control, open `scenarios/issue_8193_control.py`, trigger completion
   after `npy.`, and confirm `ndarray` appears.

Current buggy behavior: the primary scenario resolves `np` as `Unknown`, so
member completions are absent. The control resolves `npy` to the local NumPy
module.
