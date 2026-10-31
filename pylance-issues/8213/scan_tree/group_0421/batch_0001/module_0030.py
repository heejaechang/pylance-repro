"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0421.module_0030'
OFFSET = 421030

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
