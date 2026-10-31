"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0199.module_0091'
OFFSET = 199091

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
