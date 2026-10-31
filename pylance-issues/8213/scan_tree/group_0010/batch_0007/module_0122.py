"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0010.module_0122'
OFFSET = 10122

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
