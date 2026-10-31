"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0324.module_0000'
OFFSET = 324000

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
