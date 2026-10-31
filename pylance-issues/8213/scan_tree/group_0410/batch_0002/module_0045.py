"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0410.module_0045'
OFFSET = 410045

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
