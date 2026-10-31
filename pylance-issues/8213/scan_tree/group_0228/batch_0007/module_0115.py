"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0228.module_0115'
OFFSET = 228115

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
