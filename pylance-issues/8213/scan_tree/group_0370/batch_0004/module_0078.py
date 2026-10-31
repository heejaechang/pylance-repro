"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0370.module_0078'
OFFSET = 370078

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
