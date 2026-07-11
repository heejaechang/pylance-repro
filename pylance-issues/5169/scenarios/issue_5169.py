# SCENARIO: custom `python.analysis.exclude` entries should not stop automatic virtual-environment exclusion
# TARGET: the workspace diagnostics after analysis settles; support files under `venv1/Lib/site-packages` and `venv2/Lib/site-packages` are intentionally broken and should stay excluded
# TRIGGER: inspect Problems after opening this file and waiting for diagnostics to settle
# EXPECT: `.vscode/settings.json` defines `python.analysis.exclude` with only `test_packages`
# VERIFY: Problems does not report diagnostics from `venv1/Lib/site-packages/bad_module.py` or `venv2/Lib/site-packages/bad_module.py`
# RECOVER: no recovery needed

print('root file stays clean')