"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0489.module_0027'
OFFSET = 489027

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
