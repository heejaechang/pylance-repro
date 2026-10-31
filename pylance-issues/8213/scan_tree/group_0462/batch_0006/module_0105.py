"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0462.module_0105'
OFFSET = 462105

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
