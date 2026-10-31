"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0151.module_0010'
OFFSET = 151010

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
