"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0103.module_0024'
OFFSET = 103024

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
