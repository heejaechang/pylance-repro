# Issue #7428 – reportCallIssue: False error message

**Source**: https://github.com/microsoft/pylance-release/issues/7428

## Problem

When using `langchain-openai` classes (`AzureChatOpenAI`, `AzureOpenAIEmbeddings`) that inherit from Pydantic `BaseModel`, Pylance reports false "No parameter named" errors for fields like `openai_api_key` and `openai_api_version` that have `alias` set via `Field(alias="api_key")`. Pydantic accepts both the original name and the alias when `populate_by_name=True`, but Pylance only recognizes the alias.

## Setup

```bash
pip install -r requirements.txt
```

## Repro Steps (verbatim from issue)

1. Open `repro.py` in VS Code with Pylance
2. Observe diagnostics on `openai_api_version` and `openai_api_key` parameters

## Expected behavior (from user)

No error reported — Pydantic's `Field(alias="api_key")` with `populate_by_name=True` allows both the original field name and the alias as constructor parameters.

## Actual behavior (from user)

Pylance reports:
- `No parameter named "openai_api_version"` 
- `No parameter named "openai_api_key"`

## Verification Checklist

- [ ] `repro.py` shows `reportCallIssue` diagnostics on `openai_api_version` parameter
- [ ] `repro.py` shows `reportCallIssue` diagnostics on `openai_api_key` parameter
- [ ] Using the alias names (`api_version`, `api_key`) does NOT show diagnostics

## Supporting files

- `requirements.txt` — declares `langchain-openai==0.3.28` and `httpx==0.28.1` (packages the reporter uses)
- `.vscode/settings.json` — sets `typeCheckingMode: basic` per revalidation details

## Root cause

In `packages/pyright/packages/pyright-internal/src/analyzer/dataClasses.ts` line 636:
```ts
const effectiveName = entry.alias || entry.name;
```
When a `dataclass_transform` field has an alias, the alias completely replaces the field name in the synthesized `__init__`. Pydantic's `populate_by_name=True` config option (which allows BOTH original name and alias) is not supported by PEP 681 / dataclass_transform.
