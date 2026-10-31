"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0470.module_0119'
OFFSET = 470119

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
