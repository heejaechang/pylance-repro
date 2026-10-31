"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0398.module_0055'
OFFSET = 398055

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
