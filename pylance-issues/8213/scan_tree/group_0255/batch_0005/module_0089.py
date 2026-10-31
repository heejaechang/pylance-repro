"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0255.module_0089'
OFFSET = 255089

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
