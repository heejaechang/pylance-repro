"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0070.module_0059'
OFFSET = 70059

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
