"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0239.module_0108'
OFFSET = 239108

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
