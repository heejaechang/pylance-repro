"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0408.module_0024'
OFFSET = 408024

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
