"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0451.module_0096'
OFFSET = 451096

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
