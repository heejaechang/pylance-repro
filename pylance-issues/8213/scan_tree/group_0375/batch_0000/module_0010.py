"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0375.module_0010'
OFFSET = 375010

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
