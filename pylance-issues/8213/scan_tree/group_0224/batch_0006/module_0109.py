"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0224.module_0109'
OFFSET = 224109

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
