"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0226.module_0094'
OFFSET = 226094

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
