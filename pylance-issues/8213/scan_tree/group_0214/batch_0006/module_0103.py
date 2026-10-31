"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0214.module_0103'
OFFSET = 214103

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
