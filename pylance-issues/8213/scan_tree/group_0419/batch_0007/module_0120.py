"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0419.module_0120'
OFFSET = 419120

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
