"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0284.module_0033'
OFFSET = 284033

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
