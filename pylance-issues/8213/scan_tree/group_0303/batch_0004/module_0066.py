"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0303.module_0066'
OFFSET = 303066

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
