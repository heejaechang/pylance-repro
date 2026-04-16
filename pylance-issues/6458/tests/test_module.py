from tests.test_dependencies import fixture_function, another_function


def test_number_one(fixture_function):
    assert fixture_function == 1
    assert another_function() == 2