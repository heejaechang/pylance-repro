"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0387.module_0072'
OFFSET = 387072

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
