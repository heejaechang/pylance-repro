"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0051.module_0108'
OFFSET = 51108

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
