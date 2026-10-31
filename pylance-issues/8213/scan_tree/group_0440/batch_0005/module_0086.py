"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0440.module_0086'
OFFSET = 440086

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
