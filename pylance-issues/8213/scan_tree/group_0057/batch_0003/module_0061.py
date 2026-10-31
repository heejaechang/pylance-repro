"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0057.module_0061'
OFFSET = 57061

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
