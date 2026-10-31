"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0132.module_0027'
OFFSET = 132027

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
