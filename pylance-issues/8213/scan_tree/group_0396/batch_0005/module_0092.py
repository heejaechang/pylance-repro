"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0396.module_0092'
OFFSET = 396092

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
