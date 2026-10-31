"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0376.module_0018'
OFFSET = 376018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
