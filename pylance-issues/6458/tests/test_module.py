 # SCENARIO: pytest fixture imports that are consumed through fixture injection should not be dimmed as unused
 # TARGET: `fixture_function` in the import line below
 # TRIGGER: open the file with pytest installed and inspect semantic dimming
 # EXPECT: the fixture import is treated as used because the test parameter consumes it
 # VERIFY: if the import stays dimmed as unused, the bug still reproduces
 # RECOVER: no recovery needed

from tests.test_dependencies import fixture_function, another_function


def test_number_one(fixture_function):
    assert fixture_function == 1
    assert another_function() == 2