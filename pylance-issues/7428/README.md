# Issue 7428

This workspace reproduces the false `reportCallIssue` diagnostics on `langchain-openai==0.3.28` constructor aliases.

## Python version

This repro was revalidated on Python `3.12.13` with a local `.venv` interpreter in this folder.

## Setup

1. Create a Python `3.12` virtual environment in this folder.
2. Install the packages from `requirements.txt` into that environment.
3. Open this folder in VS Code and select the local `.venv` interpreter.
4. Open `scenarios/issue_7428.py` and wait for diagnostics to settle.

The workspace already sets `python.analysis.typeCheckingMode` to `basic` and `python.analysis.diagnosticMode` to `workspace`.

## Expected result

Pylance reports false `No parameter named "openai_api_version"` and `No parameter named "openai_api_key"` diagnostics on the `AzureChatOpenAI` and `AzureOpenAIEmbeddings` constructor calls.