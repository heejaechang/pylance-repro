from pytest import fixture


class Config:
    def method(self):
        pass


@fixture
def pytestconfig() -> Config:
    return Config()


class FixtureRequest:
    def __init__(self, pyfuncitem, *, _ispytest: bool = False) -> None:
        pass