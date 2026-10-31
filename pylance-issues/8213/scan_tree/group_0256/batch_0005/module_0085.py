"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0256.module_0085'
OFFSET = 256085

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
