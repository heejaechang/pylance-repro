"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0268.module_0090'
OFFSET = 268090

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
