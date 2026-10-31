"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0413.module_0048'
OFFSET = 413048

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
