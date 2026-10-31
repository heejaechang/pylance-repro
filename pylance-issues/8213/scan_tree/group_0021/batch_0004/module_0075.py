"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0021.module_0075'
OFFSET = 21075

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
