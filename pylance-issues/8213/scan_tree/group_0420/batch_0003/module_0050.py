"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0420.module_0050'
OFFSET = 420050

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
