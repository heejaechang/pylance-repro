"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0011.module_0070'
OFFSET = 11070

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
