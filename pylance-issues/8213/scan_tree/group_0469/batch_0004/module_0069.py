"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0469.module_0069'
OFFSET = 469069

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
