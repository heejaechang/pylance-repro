"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0381.module_0107'
OFFSET = 381107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
