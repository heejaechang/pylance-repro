# Issue #5689 — Intellisense not working when using pylance (no suggestions Ctrl+Space)

**Issue**: https://github.com/microsoft/pylance-release/issues/5689

## Reporter's environment

- Python 3.12.1
- Pylance v2024.3.2
- Windows 10
- Virtual environment with `simplekml==1.3.6`

## Reporter's code (verbatim excerpt)

```python
from simplekml import Kml, Snippet, Types, AltitudeMode
# Create the KML document
kml = Kml(name="Tracks", open=1)
doc = kml.newdocument(name='PMX Track', snippet=Snippet(filedate))
...
# Create a folder
fol = doc.newfolder(name='Track')

# Create a schema for extended data: heart rate, cadence and power
schema = kml.newschema()
```

## Expected behavior (verbatim)

> Intellisense working correclty with autocompletion and suggestions showing.

## Actual behavior (verbatim)

> Not a single Intellisense feature is working.
> Edit: Seems that only the simplekml library is affected and intellisense is not working for this lib.

## Bounded symptom (from investigation)

- `doc = kml.newdocument(...)` produces a `Geometry | Unknown` type under current Pylance.
- Completions at `doc.` do NOT include expected `Document` members like `newfolder`, `lookat`, `newschema`.
- The completion list is limited to `Geometry`-level members: `addfile`, `address`, `atomauthor`, etc.

## Workspace setup

- Python interpreter: `.venv/Scripts/python.exe` (Python 3.12.1)
- Package: `simplekml==1.3.6` (no py.typed; plain Python source)
- Settings: `python.analysis.typeCheckingMode: "basic"`

## Verification checklist

### Scenario 1: Completion on `doc.` (primary symptom)

1. Open `completion_doc.py`
2. Place cursor at end of line 15 (after `doc.`)
3. Invoke completion (Ctrl+Space)
4. **Expected**: Completion list contains `newfolder`
5. **Actual (reproduced)**: Completion list does NOT contain `newfolder`; limited to Geometry-level members

### Scenario 2: Reveal type of `doc`

1. Open `reveal_doc.py`
2. Wait for diagnostics to settle
3. Check the Problems panel for the `reveal_type(doc)` diagnostic
4. **Expected**: `Type of "doc" is "Document"` (the runtime type)
5. **Actual (reproduced)**: `Type of "doc" is "Geometry | Unknown"`

### Scenario 3: Code from the reporter (doc_completion.py)

1. Open `doc_completion.py`
2. Place cursor at end of line 15 (after `doc.`)
3. Invoke completion (Ctrl+Space)
4. **Expected**: Completion list contains `newschema` (from Document class)
5. **Actual (reproduced)**: Completion list does NOT contain `newschema`

## Requirements

```
simplekml==1.3.6
```

## How to set up (if re-creating)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
