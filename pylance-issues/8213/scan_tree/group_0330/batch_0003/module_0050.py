"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0330.module_0050'
OFFSET = 330050

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
