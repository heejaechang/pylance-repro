"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0353.module_0090'
OFFSET = 353090

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
