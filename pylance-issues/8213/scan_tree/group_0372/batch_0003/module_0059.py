"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0372.module_0059'
OFFSET = 372059

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
