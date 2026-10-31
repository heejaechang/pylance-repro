"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0313.module_0039'
OFFSET = 313039

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
