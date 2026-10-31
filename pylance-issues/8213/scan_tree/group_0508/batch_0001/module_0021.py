"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0508.module_0021'
OFFSET = 508021

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
