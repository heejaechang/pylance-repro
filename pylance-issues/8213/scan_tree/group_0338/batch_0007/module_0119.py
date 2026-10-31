"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0338.module_0119'
OFFSET = 338119

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
