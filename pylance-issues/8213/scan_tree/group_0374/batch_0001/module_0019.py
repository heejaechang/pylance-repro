"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0374.module_0019'
OFFSET = 374019

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
