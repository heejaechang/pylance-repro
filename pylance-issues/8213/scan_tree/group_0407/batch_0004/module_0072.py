"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0407.module_0072'
OFFSET = 407072

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
