"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0149.module_0126'
OFFSET = 149126

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
