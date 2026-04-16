# Issue 6226

This workspace reproduces the case where a compiled module ships with `.pyc` and `.pyi` files but no `.py` source file.

## Contract

- SCENARIO: compiled modules with `.pyc` and `.pyi` but no `.py` source should not trigger `reportMissingModuleSource`
- TARGET: `from compiledmod import VALUE` in `main.py`
- TRIGGER: generate `compiledmod.pyc`, then open `main.py` and inspect diagnostics on the import
- EXPECT: the import resolves without `reportMissingModuleSource`
- VERIFY: if Pylance still complains about missing module source after generating `compiledmod.pyc`, the bug still reproduces
- RECOVER: delete the generated `compiledmod.pyc` and rerun the generator when needed

## Setup

1. Run `python .\generate_compiledmod.py` in this folder.
2. Open `main.py`.
3. Inspect diagnostics on `from compiledmod import VALUE`.

The generator creates a local `compiledmod.pyc` from an embedded source string and does not leave a `.py` source file behind.
