"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0024.module_0020'
OFFSET = 24020

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
