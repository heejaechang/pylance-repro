"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0072.module_0029'
OFFSET = 72029

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
