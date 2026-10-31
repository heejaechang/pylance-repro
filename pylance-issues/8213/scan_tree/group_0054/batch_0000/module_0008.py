"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0054.module_0008'
OFFSET = 54008

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
