"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0354.module_0098'
OFFSET = 354098

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
