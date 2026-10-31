"""Open this file in VS Code while the generated scan tree is being discovered."""

from scan_tree.group_0000.batch_0000.module_0000 import make_record


def describe_fixture() -> str:
    record = make_record(3)
    return f"Synthetic scan fixture: {record['name']} -> {record['value']}"


if __name__ == "__main__":
    print(describe_fixture())
