"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0198.module_0017'
OFFSET = 198017

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
