"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0187.module_0090'
OFFSET = 187090

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
