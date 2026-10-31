"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0230.module_0066'
OFFSET = 230066

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
