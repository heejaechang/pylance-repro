"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0116.module_0053'
OFFSET = 116053

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
