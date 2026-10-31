"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0087.module_0115'
OFFSET = 87115

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
