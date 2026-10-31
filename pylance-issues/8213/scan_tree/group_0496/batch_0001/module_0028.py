"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0496.module_0028'
OFFSET = 496028

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
