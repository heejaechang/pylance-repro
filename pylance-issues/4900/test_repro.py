 # SCENARIO: unimported pytest fixtures should not gain hover info from sibling fixtures
 # TARGET: `fixture_two` in `def test_foo(fixture_two):`
 # TRIGGER: hover over `fixture_two`
 # EXPECT: the fixture type stays unknown until it is imported explicitly
 # VERIFY: if hover resolves `fixture_two` from `test_fixtures.py`, the bug still reproduces
 # RECOVER: no recovery needed

from test_fixtures import fixture_one


def test_foo(fixture_two):
    pass