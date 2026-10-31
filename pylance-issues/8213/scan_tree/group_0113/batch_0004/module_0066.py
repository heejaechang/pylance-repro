"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0113.module_0066'
OFFSET = 113066

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
