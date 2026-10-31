"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0426.module_0094'
OFFSET = 426094

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
