"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0365.module_0010'
OFFSET = 365010

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
