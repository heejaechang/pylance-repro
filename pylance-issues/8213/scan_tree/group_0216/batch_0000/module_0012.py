"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0216.module_0012'
OFFSET = 216012

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
