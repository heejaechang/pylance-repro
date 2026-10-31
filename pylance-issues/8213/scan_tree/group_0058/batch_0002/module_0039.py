"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0058.module_0039'
OFFSET = 58039

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
