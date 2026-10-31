"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0247.module_0081'
OFFSET = 247081

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
