import pytest
from toucan_presentation.person import Person


def test_init_values():
    person = Person(name="Adam", age=21)
    assert person.name == "Adam"
    assert person.age == 21


def test_introduce():
    name = "Adam"
    age = 18
    quote = f"I'm {name}.\nI'm {age}."
    person = Person(name=name, age=age)
    assert person.introduce() == quote
