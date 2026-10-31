"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0021.module_0107'
OFFSET = 21107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
