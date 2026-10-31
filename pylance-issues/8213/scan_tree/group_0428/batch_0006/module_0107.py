"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0428.module_0107'
OFFSET = 428107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
