# Issue #8293: In Pylance + Pyrefly mode, textDocument/semanticTokens/full fails on large PyTorch files

- Source: https://github.com/microsoft/pylance-release/issues/8293
- State: open
- Created: 2026-11-06T02:01:00+00:00
- Updated: 2026-11-06T02:01:00+00:00

## Reporter context

Pylance 2026.4.1, VS Code 1.144, `python.analysis.diagnosticsSource: "Pylance + Pyrefly"`, PyTorch checkout.

When I open about 20 large PyTorch files (for example `torch/_inductor/lowering.py`, `torch/_dynamo/symbolic_convert.py`, `torch/_inductor/codegen/triton.py`), `textDocument/semanticTokens/full` fails 24 times with:

```
Request textDocument/semanticTokens/full failed.
  Code: -32603
```

The stack is a deep recursion in Pylance's tree walker (`walk` / `walkMultiple` in `server.bundle.js`). Successful semantic-token requests on these files also take 2–6 s each. With the default `Pylance` diagnostics source or `Pylance + Pyright`, the same files give no failures and no slow semantic-token requests.

## Reproduction steps

Open `scenarios/issue_8293.py` in this workspace and follow the reporter steps quoted above.

## Evidence and limitations

This is extracted investigation material, not a verifier-confirmed reproduction. Only the first code block is extracted; other files, settings, dependencies and triggers may still be missing. Consult the reporter context before drawing conclusions.
