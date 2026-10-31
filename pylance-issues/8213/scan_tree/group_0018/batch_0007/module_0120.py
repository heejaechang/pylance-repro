"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0018.module_0120'
OFFSET = 18120

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
