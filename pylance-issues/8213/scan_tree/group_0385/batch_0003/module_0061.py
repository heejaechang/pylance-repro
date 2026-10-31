"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0385.module_0061'
OFFSET = 385061

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
