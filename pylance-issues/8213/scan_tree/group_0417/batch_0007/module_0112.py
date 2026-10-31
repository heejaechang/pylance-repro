"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0417.module_0112'
OFFSET = 417112

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
