"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0301.module_0035'
OFFSET = 301035

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
