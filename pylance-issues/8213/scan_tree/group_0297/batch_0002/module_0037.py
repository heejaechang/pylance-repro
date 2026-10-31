"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0297.module_0037'
OFFSET = 297037

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
