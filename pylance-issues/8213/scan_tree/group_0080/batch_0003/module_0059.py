"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0080.module_0059'
OFFSET = 80059

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
