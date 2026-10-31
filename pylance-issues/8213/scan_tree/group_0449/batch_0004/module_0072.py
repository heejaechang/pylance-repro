"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0449.module_0072'
OFFSET = 449072

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
