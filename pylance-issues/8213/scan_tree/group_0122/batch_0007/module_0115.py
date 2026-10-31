"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0122.module_0115'
OFFSET = 122115

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
