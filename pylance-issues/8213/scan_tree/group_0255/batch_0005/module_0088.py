"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0255.module_0088'
OFFSET = 255088

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
