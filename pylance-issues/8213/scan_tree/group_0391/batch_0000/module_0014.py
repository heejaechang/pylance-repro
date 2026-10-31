"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0391.module_0014'
OFFSET = 391014

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
