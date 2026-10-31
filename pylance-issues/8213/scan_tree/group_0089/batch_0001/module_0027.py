"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0089.module_0027'
OFFSET = 89027

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
