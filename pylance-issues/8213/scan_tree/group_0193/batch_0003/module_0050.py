"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0193.module_0050'
OFFSET = 193050

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
