"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0410.module_0113'
OFFSET = 410113

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
