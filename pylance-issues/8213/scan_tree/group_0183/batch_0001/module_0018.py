"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0183.module_0018'
OFFSET = 183018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
