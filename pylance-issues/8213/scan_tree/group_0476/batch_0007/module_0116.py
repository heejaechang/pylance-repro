"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0476.module_0116'
OFFSET = 476116

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
