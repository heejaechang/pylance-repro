"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0420.module_0033'
OFFSET = 420033

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
