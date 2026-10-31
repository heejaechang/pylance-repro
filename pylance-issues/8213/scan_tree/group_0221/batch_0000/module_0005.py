"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0221.module_0005'
OFFSET = 221005

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
