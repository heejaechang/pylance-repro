"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0056.module_0098'
OFFSET = 56098

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
