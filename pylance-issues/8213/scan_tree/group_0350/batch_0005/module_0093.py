"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0350.module_0093'
OFFSET = 350093

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
