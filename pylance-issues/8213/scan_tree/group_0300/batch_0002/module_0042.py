"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0300.module_0042'
OFFSET = 300042

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
