"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0485.module_0123'
OFFSET = 485123

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
