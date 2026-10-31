"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0202.module_0072'
OFFSET = 202072

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
