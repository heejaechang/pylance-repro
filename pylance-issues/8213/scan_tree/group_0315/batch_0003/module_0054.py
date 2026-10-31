"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0315.module_0054'
OFFSET = 315054

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
