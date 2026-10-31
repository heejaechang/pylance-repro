"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0068.module_0119'
OFFSET = 68119

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
