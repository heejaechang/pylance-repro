"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0242.module_0085'
OFFSET = 242085

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
