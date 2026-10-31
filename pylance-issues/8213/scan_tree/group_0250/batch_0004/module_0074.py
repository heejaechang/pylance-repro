"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0250.module_0074'
OFFSET = 250074

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
