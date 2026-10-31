"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0271.module_0048'
OFFSET = 271048

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
