 # SCENARIO: local class return inference should preserve the concrete return type
 # TARGET: the function `local_helper`
 # TRIGGER: hover over `local_helper` or inspect its inferred return type
 # EXPECT: the function is typed as returning `LocalWorker`
 # VERIFY: if the return type widens to `Any`, `Unknown`, or `None`, the bug still reproduces
 # RECOVER: no recovery needed

class LocalWorker:
    pass


def local_helper() -> LocalWorker:
    return LocalWorker()