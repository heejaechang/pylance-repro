"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0327.module_0111'
OFFSET = 327111

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
