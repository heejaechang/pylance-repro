"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0164.module_0058'
OFFSET = 164058

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
