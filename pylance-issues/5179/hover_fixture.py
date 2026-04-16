import pytest


@pytest.fixture
def fixt_1():
    """Fixture one description for hover verification."""
    yield str(42)


def test_some_test(fixt_1):
    fixt_1