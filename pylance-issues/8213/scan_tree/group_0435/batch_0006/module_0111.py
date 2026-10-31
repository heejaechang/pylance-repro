"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0435.module_0111'
OFFSET = 435111

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
