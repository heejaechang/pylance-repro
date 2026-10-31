"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0481.module_0106'
OFFSET = 481106

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
