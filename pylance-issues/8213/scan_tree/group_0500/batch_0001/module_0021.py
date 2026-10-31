"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0500.module_0021'
OFFSET = 500021

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
