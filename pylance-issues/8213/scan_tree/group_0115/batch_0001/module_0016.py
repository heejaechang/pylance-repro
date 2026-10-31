"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0115.module_0016'
OFFSET = 115016

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
