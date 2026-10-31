"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0258.module_0076'
OFFSET = 258076

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
