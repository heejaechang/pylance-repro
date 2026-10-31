"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0424.module_0125'
OFFSET = 424125

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
