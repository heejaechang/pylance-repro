"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0209.module_0032'
OFFSET = 209032

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
