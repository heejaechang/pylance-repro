"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0173.module_0035'
OFFSET = 173035

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
