"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0040.module_0107'
OFFSET = 40107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
