"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0084.module_0126'
OFFSET = 84126

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
