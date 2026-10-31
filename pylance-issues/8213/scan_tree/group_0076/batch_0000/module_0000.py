"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0076.module_0000'
OFFSET = 76000

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
