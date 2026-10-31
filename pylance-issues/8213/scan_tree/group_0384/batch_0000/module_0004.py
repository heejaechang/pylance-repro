"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0384.module_0004'
OFFSET = 384004

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
