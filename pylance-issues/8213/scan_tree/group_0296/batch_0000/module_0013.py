"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0296.module_0013'
OFFSET = 296013

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
