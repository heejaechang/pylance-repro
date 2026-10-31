"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0042.module_0005'
OFFSET = 42005

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
