# Pylance issue 8146: `os.name` inactive-code highlighting

- Issue: https://github.com/microsoft/pylance-release/issues/8146
- Title: Syntax highlighting bug after conditions with os.name as left hand side argument
- Labels: `team needs to reproduce`
- Reported environment: VS Code 1.104.3 on Windows, Remote-WSL2 Linux, Python 3.11.13, Pylance 2025.10.2

The reporter observes that syntax highlighting appears to fade or stop after a
condition with `os.name` on the left (`os.name == "nt"` or
`os.name != "nt"`), while reversing the operands avoids the effect.

Open `scenarios/issue_8146.py` in a Remote-WSL window. Compare the left- and
right-operand functions. Check whether fading is limited to code that Pylance
can prove unreachable on Linux, or incorrectly extends to reachable statements
later in the function.

