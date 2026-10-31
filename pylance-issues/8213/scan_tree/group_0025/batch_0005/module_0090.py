"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0025.module_0090'
OFFSET = 25090

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
