"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0386.module_0062'
OFFSET = 386062

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
