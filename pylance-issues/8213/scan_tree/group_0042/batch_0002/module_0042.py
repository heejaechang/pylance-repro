"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0042.module_0042'
OFFSET = 42042

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
