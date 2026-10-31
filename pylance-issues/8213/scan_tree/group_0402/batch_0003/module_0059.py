"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0402.module_0059'
OFFSET = 402059

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
