"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0117.module_0018'
OFFSET = 117018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
