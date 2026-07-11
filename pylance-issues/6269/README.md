# Issue 6269 — `reportMissingModuleSource` on native-extension submodules

Tracks https://github.com/microsoft/pylance-release/issues/6269

The minimal probe (`issue_6269_probe.py`) imports several submodules of the
`prettypretty` native extension. Runtime imports succeed, but Pyright still
reports `reportMissingModuleSource` warnings for the native submodules.

## Why this folder doesn't include the full repro tree

The verified repro requires building the `prettypretty` native extension via a
Rust toolchain, so the buildable tree (cargo + maturin + a populated `.venv`)
is hundreds of MB and is not committed here.

## Reproducing locally (WSL / Linux)

```bash
git clone https://github.com/apparebit/prettypretty.git
cd prettypretty
git checkout fc1cf50
# install rustup / rustc / cargo if missing
python -m venv .venv
. .venv/bin/activate
pip install maturin
npm install   # if needed for the dev scripts
maturin develop
# drop issue_6269_probe.py at the repo root
cp /path/to/this/folder/issue_6269_probe.py .
npm run pyright -- --pythonpath ./.venv/bin/python issue_6269_probe.py
```

Expected: `reportMissingModuleSource` warnings for `prettypretty.color.style`,
`prettypretty.color.termco`, and `prettypretty.color.theme`, even though
runtime imports succeed.
