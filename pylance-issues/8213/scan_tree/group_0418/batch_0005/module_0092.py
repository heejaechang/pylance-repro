"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0418.module_0092'
OFFSET = 418092

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
