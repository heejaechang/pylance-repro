"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0285.module_0037'
OFFSET = 285037

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
