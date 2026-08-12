# Issue 8156: Attribute docstring missing from hover for dataclass_transform field with converter

- Issue: https://github.com/microsoft/pylance-release/issues/8156
- Labels: `team needs to reproduce`
- Reported environment: Pylance 2026.3.1 (Pyright 1.1.411), Arch Linux, Python 3.14.6

The reporter observes that hovering `model.plain` includes the adjacent attribute
docstring, while hovering `model.converted` shows only its `float` type. The only
material difference is that `converted_field` receives a converter whose input
type is wider than the stored field type.

Open `scenarios/issue_8156.py` and compare hover on the final `plain` and
`converted` member accesses.
