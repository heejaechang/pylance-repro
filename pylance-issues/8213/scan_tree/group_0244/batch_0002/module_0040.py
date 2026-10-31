"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0244.module_0040'
OFFSET = 244040

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
