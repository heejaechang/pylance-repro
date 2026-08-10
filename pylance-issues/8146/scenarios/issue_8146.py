import os


def equality_left() -> str:
    before = "reachable before"
    if os.name == "nt":
        windows_only = "expected to fade on Linux"
        print(windows_only)
    after = "reachable after"
    return f"{before}: {after}"


def equality_reversed() -> str:
    before = "reachable before"
    if "nt" == os.name:
        not_statically_evaluated = "not expected to fade"
        print(not_statically_evaluated)
    after = "reachable after"
    return f"{before}: {after}"


def inequality_left_without_exit() -> str:
    if os.name != "nt":
        linux_path = "reachable on Linux"
        print(linux_path)
    after = "reachable after"
    return after


def inequality_reversed_without_exit() -> str:
    if "nt" != os.name:
        not_statically_evaluated = "not expected to fade"
        print(not_statically_evaluated)
    after = "reachable after"
    return after


def inequality_left_with_exit() -> str:
    if os.name != "nt":
        return "Linux exits here"
    windows_remainder = "expected to fade on Linux"
    return windows_remainder


def inequality_reversed_with_exit() -> str:
    if "nt" != os.name:
        return "comparison is not statically evaluated"
    remainder = "not expected to fade"
    return remainder
