"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0252.module_0118'
OFFSET = 252118

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
