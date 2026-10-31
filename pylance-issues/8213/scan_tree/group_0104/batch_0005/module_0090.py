"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0104.module_0090'
OFFSET = 104090

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
