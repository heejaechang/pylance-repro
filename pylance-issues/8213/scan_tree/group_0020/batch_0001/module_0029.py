"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0020.module_0029'
OFFSET = 20029

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
