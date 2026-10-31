"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0166.module_0065'
OFFSET = 166065

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
