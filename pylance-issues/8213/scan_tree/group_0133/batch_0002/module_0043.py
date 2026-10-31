"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0133.module_0043'
OFFSET = 133043

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
