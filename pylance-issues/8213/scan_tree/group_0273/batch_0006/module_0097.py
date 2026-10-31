"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0273.module_0097'
OFFSET = 273097

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
