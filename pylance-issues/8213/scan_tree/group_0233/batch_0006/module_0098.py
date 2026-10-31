"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0233.module_0098'
OFFSET = 233098

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
