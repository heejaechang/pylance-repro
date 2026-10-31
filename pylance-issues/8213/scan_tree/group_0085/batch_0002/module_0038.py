"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0085.module_0038'
OFFSET = 85038

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
