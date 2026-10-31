"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0338.module_0014'
OFFSET = 338014

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
