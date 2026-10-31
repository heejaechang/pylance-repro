"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0404.module_0104'
OFFSET = 404104

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
