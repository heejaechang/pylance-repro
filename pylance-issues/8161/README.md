# Pylance issue 8161: Smart Paste after an inline comment

- Issue: https://github.com/microsoft/pylance-release/issues/8161
- Setting: `"editor.pasteAs.preferences": ["text.pylance.reindent"]`
- Verification build: Pylance pre-release 2026.3.1

Open `scenarios/issue_8161.py`, copy `params = get(1)`, place the cursor
immediately after `#` on line 2, and paste normally.

The reported result inserts four spaces after `#`. During verification, the
paste produced `#params = get(1)` with no added spaces, so the issue was not
reproduced.
