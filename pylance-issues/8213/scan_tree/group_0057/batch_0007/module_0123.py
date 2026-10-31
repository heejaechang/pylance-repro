"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0057.module_0123'
OFFSET = 57123

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
