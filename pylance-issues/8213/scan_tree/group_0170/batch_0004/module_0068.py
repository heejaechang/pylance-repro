"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0170.module_0068'
OFFSET = 170068

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
