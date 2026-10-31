"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0370.module_0019'
OFFSET = 370019

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
