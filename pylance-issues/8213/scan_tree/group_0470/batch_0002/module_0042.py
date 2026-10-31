"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0470.module_0042'
OFFSET = 470042

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
