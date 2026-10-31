"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0148.module_0043'
OFFSET = 148043

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
