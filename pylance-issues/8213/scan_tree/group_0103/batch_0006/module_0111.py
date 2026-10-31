"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0103.module_0111'
OFFSET = 103111

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
