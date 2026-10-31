"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0176.module_0073'
OFFSET = 176073

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
