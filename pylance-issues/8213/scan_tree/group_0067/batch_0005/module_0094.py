"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0067.module_0094'
OFFSET = 67094

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
