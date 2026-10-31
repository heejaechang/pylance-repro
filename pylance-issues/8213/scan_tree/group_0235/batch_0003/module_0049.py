"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0235.module_0049'
OFFSET = 235049

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
