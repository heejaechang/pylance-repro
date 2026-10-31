"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0179.module_0119'
OFFSET = 179119

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
