"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0300.module_0112'
OFFSET = 300112

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
