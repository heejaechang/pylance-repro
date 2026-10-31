"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0351.module_0072'
OFFSET = 351072

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
