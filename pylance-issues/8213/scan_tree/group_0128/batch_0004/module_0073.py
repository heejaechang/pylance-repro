"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0128.module_0073'
OFFSET = 128073

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
