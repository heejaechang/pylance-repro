# Repro for https://github.com/microsoft/pylance-release/issues/8288
# Title: Workspace symbol search (#) fails for closed files when using Pylance + Pyrefly (TSP launched with --indexing-mode none)
# See README.md in this workspace for the full reporter context.

Client: Pylance shadow experiment not started: primaryUsesPyrefly.
...
TS: Launched server 29340 using runtime ...\.venv\Scripts\pyrefly.exe with args: tsp --indexing-mode none
...
FG(...): Found 326 source files
...
IDX(...): Indexing(4) started
IDX(...): scanned(4) 1406 files over 1 exec env
IDX(...): indexed(4) 1406 files over 1 exec env
IDX(...): Indexing finished(4).
