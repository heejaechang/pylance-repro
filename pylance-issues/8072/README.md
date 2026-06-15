# Repro workspace for pylance-release issue #8072

Issue: https://github.com/microsoft/pylance-release/issues/8072
Title: "Suggestions no longer support creating a docstring"
Spun off from: https://github.com/microsoft/pylance-release/issues/7767#issuecomment-4702006948

## Verbatim user report

> I have the opposite issue: I enabled `python.analysis.supportDocstringTemplate`
> (as suggested in the December 2024 release blog) but I do NOT get any
> "Generate DocString" entry in the (suggestions) popup menu when i press Ctrl+Space.
> However, if i mouse-click the bulb, then the (quick fix) popup menu DOES contain
> a "Generate Docstring" entry.
>
> SO it's definitely not working as advertised in the blog entry introducing the
> feature, because the menu entry seems to be part of the "quick fix" menu instead
> of the "suggestions" menu.
>
> Using latest stock VS Code v1.124.2 on macOS, with Pylance 2026.2.1 extension installed.

## Environment captured in the issue
- Pylance: 2026.2.1
- VS Code: 1.124.2
- OS: macOS
- Feature blog: Python in Visual Studio Code – December 2024 release

## Scaffolding added (not spelled out by reporter, but required)
- `.vscode/settings.json` enables `python.analysis.supportDocstringTemplate` (the setting the
  reporter explicitly says they enabled). It also pins `python.analysis.enableAsyncProgram` to
  `false` to match the shipped default (this setting is `experimental` and defaults to `false`),
  which is the condition under which the bug occurs.
- `example.py` provides a function (`add`) and a class (`Greeter`) each with an empty docstring
  (`""""""`) so the cursor can be placed between the opening and closing triple quotes — the exact
  position the "Generate Docstring" template completion is meant to trigger at.

## Verification checklist (in order)
1. Open this folder in VS Code with the Pylance build under test. Confirm
   `python.analysis.supportDocstringTemplate` is enabled (it is set in `.vscode/settings.json`).
2. Open `example.py`. Place the cursor between the triple quotes on line 2 (`    """|"""` inside
   `add`). Press **Ctrl+Space** to open the suggestions popup.
   - **Expected (per blog/user):** a "Generate Docstring" entry appears in the suggestions popup.
   - **Actual (reported bug):** NO "Generate Docstring" entry appears in the suggestions popup.
3. With the cursor still inside the empty docstring, open the Quick Fix / lightbulb menu
   (Ctrl+. or click the bulb).
   - **Expected & Actual:** a "Generate Docstring" entry DOES appear in the Quick Fix menu.
4. Repeat steps 2–3 inside the `Greeter` class docstring (line 7) to confirm the same
   suggestions-vs-quickfix asymmetry for a class.

The bug is confirmed when the "Generate Docstring" template entry is absent from the Ctrl+Space
suggestions list but present in the Quick Fix list, with `supportDocstringTemplate` enabled and
`enableAsyncProgram` at its default (`false`).

## Root cause (already identified by code + git history)
The docstring template completion provider (`pylance-copilot`
`DocstringTemplateCompletionProvider`) is registered with the completion registry, but PR #7587
("Implement more stuff in async mode, especially the CompletionProvider(s)", commit `e10eea8f61`)
changed that registration from the **sync** path to the **async-only** path:

```
- completionProviderRegistry?.registerProviderCtor(...)
+ completionProviderRegistry?.registerAsyncProviderCtor(...)
```

`python.analysis.enableAsyncProgram` defaults to `false`, so default-settings users run the
**sync** completion pipeline (`AggregatedCompletionProvider.getProviders()`), which consults only
the sync registry — now empty for docstring — so the suggestion never appears. The Quick Fix path
(`addGenerateDocstringCodeAction`) is independent of this registry and works in both modes, which
is exactly why the entry still shows in the lightbulb menu.

To toggle on the async path for a contrast check, set `python.analysis.enableAsyncProgram` to
`true` in `.vscode/settings.json` and repeat step 2 — the "Generate Docstring" suggestion should
then appear (confirming the sync/async parity gap).
