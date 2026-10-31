"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0026.module_0088'
OFFSET = 26088

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
