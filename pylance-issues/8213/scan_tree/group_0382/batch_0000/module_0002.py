"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0382.module_0002'
OFFSET = 382002

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
