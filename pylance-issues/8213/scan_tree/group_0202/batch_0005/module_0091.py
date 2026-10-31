"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0202.module_0091'
OFFSET = 202091

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
