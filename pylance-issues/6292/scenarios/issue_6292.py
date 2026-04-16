# SCENARIO: go to definition on a fixture-provided method call inside a test class should resolve to the method implementation
# TARGET: `params_navigation` in `fixture_from_main.params_navigation()` inside `TestClassTest.test_without_method_definition` below, not the top-level test function call
# TRIGGER: Go to Definition
# EXPECT: hover on the target shows a method on `HomePage`
# VERIFY: after Go to Definition, the active editor lands on `def params_navigation(self):` below
# RECOVER: navigate back to the original test file if a new location is opened

import pytest


class HomePage:
    def params_navigation(self):
        """Method description."""
        print('params_navigation')


@pytest.fixture
def fixture_from_main() -> HomePage:
    return HomePage()


class TestClassTest:
    def test_without_method_definition(self, fixture_from_main):
        fixture_from_main.params_navigation()


def test_with_method_definition(fixture_from_main):
    fixture_from_main.params_navigation()