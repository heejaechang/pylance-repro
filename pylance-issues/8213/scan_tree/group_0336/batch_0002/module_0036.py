"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0336.module_0036'
OFFSET = 336036

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
