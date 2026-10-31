"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0077.module_0082'
OFFSET = 77082

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
