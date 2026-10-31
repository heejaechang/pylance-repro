"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0111.module_0026'
OFFSET = 111026

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
