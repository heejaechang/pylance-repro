"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0240.module_0028'
OFFSET = 240028

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
