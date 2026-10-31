"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0018.module_0124'
OFFSET = 18124

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
