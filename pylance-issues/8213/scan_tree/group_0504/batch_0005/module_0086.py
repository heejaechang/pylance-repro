"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0504.module_0086'
OFFSET = 504086

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
