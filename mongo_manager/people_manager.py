from typing import List
from models.person_model import Person
from mongo_manager import exceptions


def get_people() -> List[Person]:
    return Person.objects.all()


def get_person(username: str) -> Person:
    return Person.objects(username=username).first()


def user_exists(username: str) -> bool:
    return Person.objects(username=username).count() > 0


def initiate_user(username: str):
    if user_exists(username):
        raise exceptions.UserAlreadyExistsException("user already exists")
    person = Person(username)
    person.save()
    return person
