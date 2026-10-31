"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0281.module_0033'
OFFSET = 281033

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
