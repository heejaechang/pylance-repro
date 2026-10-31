"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0245.module_0066'
OFFSET = 245066

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
