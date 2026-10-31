"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0318.module_0017'
OFFSET = 318017

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
