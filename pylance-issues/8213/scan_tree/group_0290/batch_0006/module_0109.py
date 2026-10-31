"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0290.module_0109'
OFFSET = 290109

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
