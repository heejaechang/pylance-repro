"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0225.module_0033'
OFFSET = 225033

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
