"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0058.module_0063'
OFFSET = 58063

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
