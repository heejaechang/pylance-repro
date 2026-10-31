"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0035.module_0078'
OFFSET = 35078

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
