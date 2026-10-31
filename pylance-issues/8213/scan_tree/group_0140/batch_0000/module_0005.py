"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0140.module_0005'
OFFSET = 140005

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
