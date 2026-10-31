"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0485.module_0113'
OFFSET = 485113

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
