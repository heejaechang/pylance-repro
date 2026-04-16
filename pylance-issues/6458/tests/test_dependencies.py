import pytest


@pytest.fixture(scope='function')
def fixture_function():
    yield 1


def another_function():
    return 2