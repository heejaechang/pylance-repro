"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0088.module_0040'
OFFSET = 88040

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
