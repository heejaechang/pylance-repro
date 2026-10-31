"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0023.module_0061'
OFFSET = 23061

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
