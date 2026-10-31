"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0356.module_0087'
OFFSET = 356087

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
