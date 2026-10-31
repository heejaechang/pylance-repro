"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0267.module_0107'
OFFSET = 267107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
