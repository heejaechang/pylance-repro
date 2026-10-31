"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0488.module_0059'
OFFSET = 488059

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
