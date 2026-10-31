"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0154.module_0109'
OFFSET = 154109

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
