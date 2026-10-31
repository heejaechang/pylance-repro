"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0384.module_0085'
OFFSET = 384085

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
