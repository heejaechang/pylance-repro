"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0472.module_0064'
OFFSET = 472064

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
