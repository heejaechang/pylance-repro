"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0434.module_0006'
OFFSET = 434006

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
