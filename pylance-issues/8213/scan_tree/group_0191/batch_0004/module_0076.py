"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0191.module_0076'
OFFSET = 191076

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
