"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0424.module_0066'
OFFSET = 424066

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
