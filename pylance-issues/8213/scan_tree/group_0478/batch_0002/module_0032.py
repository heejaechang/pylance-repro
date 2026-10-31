"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0478.module_0032'
OFFSET = 478032

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
