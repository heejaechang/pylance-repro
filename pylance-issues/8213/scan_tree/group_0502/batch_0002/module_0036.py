"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0502.module_0036'
OFFSET = 502036

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
