"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0029.module_0037'
OFFSET = 29037

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
