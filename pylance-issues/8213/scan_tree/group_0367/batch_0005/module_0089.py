"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0367.module_0089'
OFFSET = 367089

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
