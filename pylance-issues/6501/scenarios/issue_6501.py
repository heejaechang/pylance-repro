# SCENARIO: parameter-name inlay hints should support navigation to the callee parameter definition
# TARGET: the rendered `alpha=`, `beta=`, `gamma=`, or `delta=` call-argument-name inlay hints on the call below
# TRIGGER: interact with a rendered parameter-name inlay hint
# EXPECT: navigation should land on the corresponding parameter definition, or an equivalent definition target
# VERIFY: if interaction leaves the cursor on the call line with no definition navigation, the requested behavior is still absent
# RECOVER: no recovery needed

from pathlib import Path


def method(
    alpha: int,
    beta: str,
    gamma: Path,
    delta: int | None = None,
) -> None:
    pass


value = method(10, 'hello', Path('path'), None)