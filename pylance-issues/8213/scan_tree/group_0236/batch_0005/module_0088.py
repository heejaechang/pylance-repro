"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0236.module_0088'
OFFSET = 236088

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
