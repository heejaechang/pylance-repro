"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0205.module_0011'
OFFSET = 205011

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
