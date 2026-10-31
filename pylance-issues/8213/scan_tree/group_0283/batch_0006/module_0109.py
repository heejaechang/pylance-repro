"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0283.module_0109'
OFFSET = 283109

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
