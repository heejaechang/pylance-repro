"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0477.module_0050'
OFFSET = 477050

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
