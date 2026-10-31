"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0306.module_0104'
OFFSET = 306104

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
