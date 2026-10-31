"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0423.module_0024'
OFFSET = 423024

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
