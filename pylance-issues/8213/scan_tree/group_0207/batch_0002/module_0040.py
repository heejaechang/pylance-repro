"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0207.module_0040'
OFFSET = 207040

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
