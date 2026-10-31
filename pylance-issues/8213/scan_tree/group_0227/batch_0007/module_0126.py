"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0227.module_0126'
OFFSET = 227126

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
