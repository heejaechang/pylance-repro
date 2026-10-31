"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0440.module_0067'
OFFSET = 440067

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
