"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0383.module_0078'
OFFSET = 383078

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
