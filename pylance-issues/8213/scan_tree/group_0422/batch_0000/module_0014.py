"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0422.module_0014'
OFFSET = 422014

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
