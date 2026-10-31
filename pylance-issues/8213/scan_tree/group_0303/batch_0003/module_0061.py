"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0303.module_0061'
OFFSET = 303061

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
