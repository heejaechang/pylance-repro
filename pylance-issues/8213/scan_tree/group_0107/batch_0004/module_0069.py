"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0107.module_0069'
OFFSET = 107069

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
