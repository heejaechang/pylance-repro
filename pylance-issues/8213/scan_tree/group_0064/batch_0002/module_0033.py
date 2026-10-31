"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0064.module_0033'
OFFSET = 64033

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
