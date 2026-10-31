"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0452.module_0038'
OFFSET = 452038

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
