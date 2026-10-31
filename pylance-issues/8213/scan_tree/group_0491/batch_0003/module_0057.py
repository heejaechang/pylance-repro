"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0491.module_0057'
OFFSET = 491057

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
