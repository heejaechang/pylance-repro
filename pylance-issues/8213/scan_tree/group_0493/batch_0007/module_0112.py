"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0493.module_0112'
OFFSET = 493112

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
