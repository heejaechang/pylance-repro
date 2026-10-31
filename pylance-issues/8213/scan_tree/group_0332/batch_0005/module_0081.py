"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0332.module_0081'
OFFSET = 332081

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
