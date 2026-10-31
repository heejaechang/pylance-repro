"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0377.module_0068'
OFFSET = 377068

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
