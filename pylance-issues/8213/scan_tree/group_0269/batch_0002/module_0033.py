"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0269.module_0033'
OFFSET = 269033

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
