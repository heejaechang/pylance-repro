"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0335.module_0071'
OFFSET = 335071

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
