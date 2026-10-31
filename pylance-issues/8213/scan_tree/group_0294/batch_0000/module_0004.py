"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0294.module_0004'
OFFSET = 294004

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
