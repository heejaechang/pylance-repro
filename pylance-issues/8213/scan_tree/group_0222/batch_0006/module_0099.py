"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0222.module_0099'
OFFSET = 222099

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
