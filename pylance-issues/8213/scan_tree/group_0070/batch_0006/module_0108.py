"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0070.module_0108'
OFFSET = 70108

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
