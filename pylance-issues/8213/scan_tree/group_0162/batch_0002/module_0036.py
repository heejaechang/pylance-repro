"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0162.module_0036'
OFFSET = 162036

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
