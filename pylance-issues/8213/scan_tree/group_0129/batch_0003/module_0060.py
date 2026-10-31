"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0129.module_0060'
OFFSET = 129060

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
