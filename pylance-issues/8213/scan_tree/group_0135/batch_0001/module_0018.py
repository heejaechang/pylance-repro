"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0135.module_0018'
OFFSET = 135018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
