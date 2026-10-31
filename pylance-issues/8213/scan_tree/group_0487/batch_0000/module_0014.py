"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0487.module_0014'
OFFSET = 487014

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
