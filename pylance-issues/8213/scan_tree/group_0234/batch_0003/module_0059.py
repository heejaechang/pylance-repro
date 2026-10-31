"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0234.module_0059'
OFFSET = 234059

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
