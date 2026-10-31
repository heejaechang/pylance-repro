"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0063.module_0014'
OFFSET = 63014

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
