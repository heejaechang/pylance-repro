"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0161.module_0057'
OFFSET = 161057

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
