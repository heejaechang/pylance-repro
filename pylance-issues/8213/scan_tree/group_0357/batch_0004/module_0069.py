"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0357.module_0069'
OFFSET = 357069

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
