"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0497.module_0085'
OFFSET = 497085

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
