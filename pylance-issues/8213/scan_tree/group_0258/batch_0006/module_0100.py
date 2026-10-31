"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0258.module_0100'
OFFSET = 258100

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
