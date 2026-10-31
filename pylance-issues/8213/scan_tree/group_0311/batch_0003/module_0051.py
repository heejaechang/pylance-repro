"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0311.module_0051'
OFFSET = 311051

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
