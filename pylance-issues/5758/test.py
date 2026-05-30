from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


p: Person = {"name": "Alice", "age": 30}
print(p.name)
