"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0306.module_0073'
OFFSET = 306073

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
