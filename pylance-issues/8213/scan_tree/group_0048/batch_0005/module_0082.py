"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0048.module_0082'
OFFSET = 48082

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
