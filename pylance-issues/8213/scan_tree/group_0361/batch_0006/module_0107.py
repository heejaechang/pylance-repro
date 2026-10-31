"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0361.module_0107'
OFFSET = 361107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
