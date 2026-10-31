"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0151.module_0125'
OFFSET = 151125

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
