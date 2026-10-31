"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0218.module_0084'
OFFSET = 218084

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
