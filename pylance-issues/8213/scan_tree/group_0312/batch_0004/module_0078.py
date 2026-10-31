"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0312.module_0078'
OFFSET = 312078

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
