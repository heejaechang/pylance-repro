"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0405.module_0086'
OFFSET = 405086

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
