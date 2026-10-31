"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0435.module_0127'
OFFSET = 435127

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
