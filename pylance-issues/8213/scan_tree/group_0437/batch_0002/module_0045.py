"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0437.module_0045'
OFFSET = 437045

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
