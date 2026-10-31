"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0040.module_0016'
OFFSET = 40016

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
