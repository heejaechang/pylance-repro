"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0466.module_0047'
OFFSET = 466047

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
