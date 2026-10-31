"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0418.module_0053'
OFFSET = 418053

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
