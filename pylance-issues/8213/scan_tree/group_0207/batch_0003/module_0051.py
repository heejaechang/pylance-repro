"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0207.module_0051'
OFFSET = 207051

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
