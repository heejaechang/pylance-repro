"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0122.module_0047'
OFFSET = 122047

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
