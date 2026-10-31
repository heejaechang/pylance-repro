"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0155.module_0066'
OFFSET = 155066

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
