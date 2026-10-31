"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0251.module_0028'
OFFSET = 251028

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
