"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0082.module_0088'
OFFSET = 82088

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
