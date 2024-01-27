from typing import List, Optional, Tuple

import pymongo
from pymongo import database
import mongoengine
import yaml

client: Optional[pymongo.MongoClient] = None
db: Optional[pymongo.database.Database] = None


def setup(config_file: str = "configuration.yaml"):
    global client, db

    db_config = yaml.safe_load(open(config_file))["databases"]["mongo"]

    mongo_uri = f"mongodb://{db_config['host']}:{db_config['port']}"
    client = pymongo.MongoClient(
        mongo_uri,
        username=db_config["user"],
        password=db_config["password"],
        authSource="tasky",
        authMechanism="SCRAM-SHA-1",
    )
    db = client["tasky"]


def setup_orm():
    db_config = yaml.safe_load(open("configuration.yaml"))["databases"]["mongo"]
    mongoengine.connect(
        db_config["database"],
        username=db_config["user"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config["port"],
        authentication_source="tasky",
        authentication_mechanism="SCRAM-SHA-1",
    )


def get_people() -> List[Tuple[str, str]]:
    collection = db["people"]
    people = collection.find({}, {"_id": 0})
    return [(person["username"], person["state"]) for person in people]


if __name__ == '__main__':
    setup()
    p = get_people()
    for pp in p:
        print(pp)
