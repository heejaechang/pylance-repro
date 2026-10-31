"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0048.module_0066'
OFFSET = 48066

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
