"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0133.module_0024'
OFFSET = 133024

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
