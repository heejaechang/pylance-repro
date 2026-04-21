# Issue 5542

This workspace reproduces the incorrect async override completion return annotation described in issue 5542.

## Python version

This repro was revalidated on current bits with a local Python `3.12+` interpreter and no third-party dependencies.

## Setup

1. Create a local Python virtual environment in this folder.
2. Open this folder in VS Code and select the local `.venv` interpreter.
3. Open `scenarios/issue_5542.py`.
4. In class `Derived`, place the cursor at the end of `async def ya`, request completions, and commit `yadda`.

The workspace already sets `python.analysis.typeCheckingMode` to `off` to keep the repro focused on override-completion generation.

## Expected result

Pylance still reproduces the issue by generating:

```python
async def yadda(self) -> Awaitable[int]:
    return super().yadda()
```

instead of the correct async override signature:

```python
async def yadda(self) -> int:
    return await super().yadda()
```

## Secondary note

The related `AsyncContextManager.__aenter__` variant from the issue thread has drifted on current bits: it no longer generates the old `Coroutine[...]` form, but it still produces the wrong return annotation (`Any` instead of `Self`). The retained workspace keeps the primary minimal Awaitable-based contract because it remains the clearest still-repro case.
