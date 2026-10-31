"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0357.module_0043'
OFFSET = 357043

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
