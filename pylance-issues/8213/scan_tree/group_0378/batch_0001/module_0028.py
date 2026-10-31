"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0378.module_0028'
OFFSET = 378028

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
