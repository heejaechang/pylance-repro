"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0500.module_0065'
OFFSET = 500065

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
