"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0445.module_0042'
OFFSET = 445042

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
