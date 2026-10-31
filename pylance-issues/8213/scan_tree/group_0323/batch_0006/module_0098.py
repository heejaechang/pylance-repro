"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0323.module_0098'
OFFSET = 323098

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
