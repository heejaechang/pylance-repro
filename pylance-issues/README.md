# pylance-issues

This folder contains issue repro workspaces.

Open the folder for an issue and follow that folder's README to rerun the scenario.

## Folder Naming

- Use `pylance-issues/<issue>` for a normal issue workspace.
- Use `pylance-issues/<issue>-draft` when the scenario is still being confirmed.

## Current Set

- Issue folders: 109
- Standard issue folders: 108
- Draft folders: `7554-draft`
- Issues without folders yet: `4970`, `5737`, `6086`

## Workspace Notes

- Some folders include `.vscode/settings.json` or helper files that are useful while reproducing the issue.
- If a scenario depends on a specific interpreter or environment, select the appropriate one for your machine before rerunning it.
- `5808/` is the notebook-focused workspace to use for that issue.

## Scenario Notes

- `5410/` contains the pytest fixture hover scenario in `hover_fixture.py`.
- `6144/` contains the comment-sensitive Extract Method scenario in `main.py`.
- `7295/` contains the external-edit semantic-highlighting lag scenario in `fileWatcher.py`.

## Draft Folder

- `7554-draft/` is still useful for investigation, but the scenario needs stronger confirmation before it should be treated as final.

## Not Present

- `4970`, `5737`, and `6086` do not have folders in this repo yet.
