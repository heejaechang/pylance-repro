"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0446.module_0006'
OFFSET = 446006

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
