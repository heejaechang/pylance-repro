"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0310.module_0004'
OFFSET = 310004

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
