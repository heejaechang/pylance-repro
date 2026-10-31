"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0046.module_0084'
OFFSET = 46084

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
