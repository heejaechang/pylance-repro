"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0448.module_0051'
OFFSET = 448051

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
