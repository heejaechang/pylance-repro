"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0340.module_0055'
OFFSET = 340055

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
