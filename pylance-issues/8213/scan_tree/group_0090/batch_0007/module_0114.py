"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0090.module_0114'
OFFSET = 90114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
