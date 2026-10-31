"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0195.module_0039'
OFFSET = 195039

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
