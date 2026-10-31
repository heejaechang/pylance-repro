"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0460.module_0046'
OFFSET = 460046

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
