"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0069.module_0007'
OFFSET = 69007

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
