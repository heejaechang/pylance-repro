"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0407.module_0096'
OFFSET = 407096

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
