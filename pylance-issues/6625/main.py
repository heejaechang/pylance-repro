import typing


class C(typing.TypedDict):
    abc: str


c: C = {}
c.update({"": ""})
c |= {"": ""}