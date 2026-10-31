"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0075.module_0084'
OFFSET = 75084

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
