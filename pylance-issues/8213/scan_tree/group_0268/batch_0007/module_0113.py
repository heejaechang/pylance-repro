"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0268.module_0113'
OFFSET = 268113

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
