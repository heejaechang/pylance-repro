"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0362.module_0091'
OFFSET = 362091

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
