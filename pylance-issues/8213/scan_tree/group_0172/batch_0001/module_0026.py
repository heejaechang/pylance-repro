"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0172.module_0026'
OFFSET = 172026

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
