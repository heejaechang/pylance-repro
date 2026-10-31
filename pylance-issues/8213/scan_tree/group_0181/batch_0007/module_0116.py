"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0181.module_0116'
OFFSET = 181116

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
