"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0130.module_0015'
OFFSET = 130015

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
