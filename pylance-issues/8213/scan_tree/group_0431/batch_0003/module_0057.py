"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0431.module_0057'
OFFSET = 431057

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
