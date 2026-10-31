"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0495.module_0012'
OFFSET = 495012

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
