"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0441.module_0067'
OFFSET = 441067

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
