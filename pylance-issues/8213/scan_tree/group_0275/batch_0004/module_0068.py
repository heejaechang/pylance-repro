"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0275.module_0068'
OFFSET = 275068

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
