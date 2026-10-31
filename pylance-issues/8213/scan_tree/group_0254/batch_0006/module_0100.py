"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0254.module_0100'
OFFSET = 254100

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
