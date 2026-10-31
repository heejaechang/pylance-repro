"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0005.module_0053'
OFFSET = 5053

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
