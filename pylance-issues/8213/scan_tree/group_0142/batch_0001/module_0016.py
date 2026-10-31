"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0142.module_0016'
OFFSET = 142016

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
