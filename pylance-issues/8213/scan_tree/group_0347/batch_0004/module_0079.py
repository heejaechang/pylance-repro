"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0347.module_0079'
OFFSET = 347079

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
