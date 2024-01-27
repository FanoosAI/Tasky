from typing import List, Tuple
import mongo_manager
from models.person_model import Person


def _collection():
    return mongo_manager.db["people"]


def get_people() -> List[Tuple[str, str]]:
    people = _collection().find({}, {"_id": 0})
    return [(person["username"], person["state"]) for person in people]


def user_exists(username: str) -> bool:
    return _collection().find_one({"username": username}) is not None


def initiate_user(username: str):
    person = Person(username)
    # collection.insert_one(person.__dict__)
    return person


