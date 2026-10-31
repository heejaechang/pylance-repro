"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0032.module_0067'
OFFSET = 32067

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
