"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0132.module_0106'
OFFSET = 132106

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
