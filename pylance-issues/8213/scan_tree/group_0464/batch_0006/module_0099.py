"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0464.module_0099'
OFFSET = 464099

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
