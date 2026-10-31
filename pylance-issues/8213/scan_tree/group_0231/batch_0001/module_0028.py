"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0231.module_0028'
OFFSET = 231028

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
