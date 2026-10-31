"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0487.module_0080'
OFFSET = 487080

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
