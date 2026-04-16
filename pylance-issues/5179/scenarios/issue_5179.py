# SCENARIO: pytest fixture completion should work even when no prefix has been typed yet
# TARGET: the empty parameter slot in `def test_uses_fixture():` below
# TRIGGER: Completion
# EXPECT: the file defines a local pytest fixture named `my_fixture`
# VERIFY: the completion list at the empty parameter slot includes `my_fixture` before any prefix is typed
# RECOVER: no recovery needed

import pytest


@pytest.fixture
def my_fixture() -> str:
    return 'fixture'


def test_uses_fixture():
    pass