"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0088.module_0061'
OFFSET = 88061

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
