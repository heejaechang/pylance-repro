"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0403.module_0098'
OFFSET = 403098

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
