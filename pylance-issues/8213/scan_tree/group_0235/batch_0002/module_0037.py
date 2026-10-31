"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0235.module_0037'
OFFSET = 235037

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
