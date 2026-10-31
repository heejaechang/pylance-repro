"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0099.module_0104'
OFFSET = 99104

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
