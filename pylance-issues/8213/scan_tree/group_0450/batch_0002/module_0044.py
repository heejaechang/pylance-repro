"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0450.module_0044'
OFFSET = 450044

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
