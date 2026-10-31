"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0028.module_0046'
OFFSET = 28046

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
