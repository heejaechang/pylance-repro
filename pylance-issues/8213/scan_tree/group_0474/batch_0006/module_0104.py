"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0474.module_0104'
OFFSET = 474104

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
