"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0426.module_0013'
OFFSET = 426013

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
