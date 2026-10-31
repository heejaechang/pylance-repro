"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0458.module_0056'
OFFSET = 458056

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
