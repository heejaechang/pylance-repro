"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0083.module_0074'
OFFSET = 83074

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
