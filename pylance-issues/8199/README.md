# Diagnostics for Python embedded in Brython HTML

Issue: https://github.com/microsoft/pylance-release/issues/8199

Related feature: https://github.com/microsoft/pylance-release/issues/6760

This workspace separates working Brython IntelliSense from diagnostics that
should appear on the HTML file containing the Python code.

## Setup

Install the VS Code Python and Pylance extensions and select a Python
interpreter. No third-party Python packages are required.
If VS Code exposes separate Python and Pylance interpreter selectors,
confirm that both select the same environment.

Use a Pylance build that includes Brython runtime type information. The
scenario is intended for Pylance 2026.3.103. As of September 11, 2026,
the latest public release is 2026.3.102; the discussion linked above notes
that its Brython type information is incomplete. No extension binaries
are included here.

Open this directory itself as the VS Code workspace, not the repository root.
The checked-in workspace settings enable HTML-embedded Python and basic
type checking:

```json
{
    "python.analysis.supportHtmlEmbeddedPython": true,
    "python.analysis.typeCheckingMode": "basic"
}
```

Reload the VS Code window if these settings were changed after opening HTML.

## Reproduction steps

1. Open `control.py` first to activate Pylance.
2. Confirm that Problems reports the incompatible assignment in
   `label: str = 42`. This is an intentional control error.
3. Open `index.html`. Keep its language mode set to HTML.
4. Hover over `button.bind`, or place the caret immediately after the dot
   and press Ctrl+Space. Brython's `bind` member should be available.
5. Inspect `document <= object()` in the same script block.
6. Open Problems and filter to `index.html`.
7. If the diagnostic is absent, run **Pylance: Restart Language Server**,
   reopen `index.html`, and inspect Problems again.

## Expected behavior

`document <= object()` produces an error on `index.html`:

```text
Operator "<=" not supported for types "DOMNode" and "object"
```

The valid Brython import should not produce an unresolved-import error.
The ordinary Python control error should remain associated with `control.py`.

## Observed behavior

On September 11, 2026, Problems filtered to `index.html` showed:

```text
Showing 0 of 1
No results found with provided filter criteria.
```

The sole unfiltered problem was the intentional assignment error in
`control.py`. There was no error for `document <= object()` and no unresolved
`browser` import. The HTML diagnostic remained absent after restarting
Pylance, closing and reopening HTML, and waiting for analysis to settle.

Hover over `button.bind` did show Brython type information:

```text
def bind(
    event: str,
    callback: (DOMEvent) -> object,
    options: bool | dict[str, Any] | None = ...
) -> None
```

## Recorded environment

| Component | Version |
| --- | --- |
| Pylance candidate | 2026.3.103 |
| VS Code | 1.137.0 |
| Python extension | 2026.4.0 |
| Python | 3.14.4, x64 |
| OS | Windows 11, build 26200 |

The file stayed in HTML language mode. Basic type checking and the
HTML-embedded Python setting were enabled.

## Evidence and limitations

This is an editor-only scenario. Do not execute the embedded code with CPython.
It targets Brython's browser-specific types, so installing an unrelated PyPI
package named `browser` would change the scenario.

The HTML is intentionally not a complete browser application: no runtime
scripts, network requests, or browser execution are necessary to reproduce
editor diagnostics. The example does not assume a cause for a missing
diagnostic. The recorded behavior does not distinguish between missing
diagnostics on the embedded document and failure to show them on the HTML source.
