# Issue #7970: Hovering over instance of derived class shows docstring for base class

- Source: https://github.com/microsoft/pylance-release/issues/7970
- State: open
- Created: 2026-04-07T05:12:33+00:00
- Updated: 2026-04-07T16:32:43+00:00
- Labels: enhancement, ai-triage-responded

## Reporter context

<!--
Read the guidelines for filing an issue first.

https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#filing-an-issue
-->

## Environment data

<!--
To find your version, open the VS Code extensions panel, then locate Pylance from the list of installed extensions. The version appears next to the name.
-->

-   Pylance version: 2025.6.2
-   OS and version: Mac 14.7.5
-   Python version (& distribution if applicable, e.g. Anaconda): 3.13

## Code Snippet

<!--
Please provide a minimal, self-contained code snippet that reproduces the issue. If the code snippet uses any libraries, please specify the versions used.

Note: If you think a GIF of what is happening would be helpful, consider tools like https://github.com/vkohaupt/vokoscreenNG, https://www.cockos.com/licecap/, https://github.com/phw/peek or https://www.screentogif.com/ .
-->

```python
def test():
    raise NotImplementedError()
```

## Repro Steps

<!--
If multiple steps are needed to reproduce the issue, please list the steps here. Delete this section if not needed.
-->

1. Hover over the `NotImplementedError` in the code snippet within vscode.

## Expected behavior

Docstring for `NotImplementedError` would appear in the popup.

## Actual behavior

Docstring for base class `BaseException` appears:

<img width="824" height="212" alt="Image" src="https://github.com/user-attachments/assets/b7301f60-c98a-4bb4-8c79-426ab85e7adc" />

## Logs

<!--
Enable trace logging by adding "python.analysis.logLevel": "Trace" to your settings.json configuration file.

Adding this will cause a large amount of info to be printed to the Python output panel. This should not be left long term, as the performance impact of the logging is significant.
-->

```
XXX
```
