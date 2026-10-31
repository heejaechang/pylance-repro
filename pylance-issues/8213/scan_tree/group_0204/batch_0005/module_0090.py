"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0204.module_0090'
OFFSET = 204090

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
