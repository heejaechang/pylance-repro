"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0308.module_0044'
OFFSET = 308044

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
