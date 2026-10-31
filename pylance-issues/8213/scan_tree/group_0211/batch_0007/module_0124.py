"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0211.module_0124'
OFFSET = 211124

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
