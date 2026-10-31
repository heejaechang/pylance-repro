"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0181.module_0086'
OFFSET = 181086

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
