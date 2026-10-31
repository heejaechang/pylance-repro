"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0056.module_0042'
OFFSET = 56042

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
