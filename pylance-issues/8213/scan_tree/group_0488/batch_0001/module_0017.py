"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0488.module_0017'
OFFSET = 488017

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
