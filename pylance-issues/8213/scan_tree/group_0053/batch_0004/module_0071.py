"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0053.module_0071'
OFFSET = 53071

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
