"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0169.module_0021'
OFFSET = 169021

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
