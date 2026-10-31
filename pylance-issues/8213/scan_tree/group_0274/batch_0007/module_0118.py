"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0274.module_0118'
OFFSET = 274118

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
