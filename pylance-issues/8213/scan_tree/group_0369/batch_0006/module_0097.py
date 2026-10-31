"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0369.module_0097'
OFFSET = 369097

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
