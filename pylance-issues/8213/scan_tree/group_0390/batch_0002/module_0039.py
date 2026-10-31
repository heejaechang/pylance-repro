"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0390.module_0039'
OFFSET = 390039

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
