"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0336.module_0112'
OFFSET = 336112

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
