"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0224.module_0115'
OFFSET = 224115

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
