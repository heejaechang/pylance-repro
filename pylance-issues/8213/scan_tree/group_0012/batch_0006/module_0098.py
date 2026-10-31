"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0012.module_0098'
OFFSET = 12098

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
