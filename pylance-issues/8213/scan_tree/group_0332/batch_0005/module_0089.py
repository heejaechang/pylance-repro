"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0332.module_0089'
OFFSET = 332089

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
