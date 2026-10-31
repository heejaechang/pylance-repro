"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0353.module_0047'
OFFSET = 353047

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
