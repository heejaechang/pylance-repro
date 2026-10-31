"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0323.module_0018'
OFFSET = 323018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
