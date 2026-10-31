"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0338.module_0074'
OFFSET = 338074

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
