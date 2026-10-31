"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0466.module_0124'
OFFSET = 466124

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
