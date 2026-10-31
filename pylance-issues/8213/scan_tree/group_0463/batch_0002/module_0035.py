"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0463.module_0035'
OFFSET = 463035

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
