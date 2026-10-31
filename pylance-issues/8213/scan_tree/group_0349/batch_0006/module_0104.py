"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0349.module_0104'
OFFSET = 349104

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
