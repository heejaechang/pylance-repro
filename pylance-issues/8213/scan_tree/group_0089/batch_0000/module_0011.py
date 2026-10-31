"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0089.module_0011'
OFFSET = 89011

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
