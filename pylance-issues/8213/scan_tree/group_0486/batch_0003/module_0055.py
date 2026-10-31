"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0486.module_0055'
OFFSET = 486055

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
