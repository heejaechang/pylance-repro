"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0400.module_0040'
OFFSET = 400040

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
