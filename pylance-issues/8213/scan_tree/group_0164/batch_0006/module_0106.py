"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0164.module_0106'
OFFSET = 164106

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
