"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0093.module_0089'
OFFSET = 93089

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
