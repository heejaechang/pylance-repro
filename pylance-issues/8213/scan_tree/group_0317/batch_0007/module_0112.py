"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0317.module_0112'
OFFSET = 317112

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
