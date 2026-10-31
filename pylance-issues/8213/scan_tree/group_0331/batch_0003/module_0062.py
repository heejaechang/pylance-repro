"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0331.module_0062'
OFFSET = 331062

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
