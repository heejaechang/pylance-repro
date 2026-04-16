# SCENARIO: chained pytest yield fixtures should preserve member types for the yielded object inside the test body
# TARGET: the gap after `fixt_2.` in `fixt_2.` below inside `test_some_test`
# TRIGGER: Completion
# EXPECT: completion opens on the chained fixture object in the test body
# VERIFY: the suggestion list includes `some_f2` and `obj1` for the yielded `Cl_2` instance instead of losing the type and offering no useful members
# RECOVER: no recovery needed

import pytest


class Cl_1:
    def some_f1(self) -> None:
        pass


class Cl_2:
    def __init__(self):
        self.obj1 = Cl_1()

    def some_f2(self) -> None:
        pass


@pytest.fixture
def fixt_1():
    yield Cl_2()


@pytest.fixture
def fixt_2(fixt_1):
    yield fixt_1


def test_some_test(fixt_2):
    fixt_2.