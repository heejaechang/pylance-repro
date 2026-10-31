"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0084.module_0058'
OFFSET = 84058

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
