# SCENARIO: a fixture injected into another fixture should keep its member type and completions inside the fixture body
# TARGET: the gap after `mocker.` inside `myfixture` below
# TRIGGER: Completion
# EXPECT: completion opens at the fixture-parameter member access inside the fixture body
# VERIFY: the suggestion list includes `patch` for the yielded fixture object instead of showing no useful member completions
# RECOVER: no recovery needed

import pytest


class Helper:
    def patch(self) -> None:
        pass


@pytest.fixture
def mocker():
    yield Helper()


@pytest.fixture
def myfixture(mocker):
    mocker.
    yield mocker