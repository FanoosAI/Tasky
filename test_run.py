import mongo_manager
from mongo_manager.people_manager import *
from models import person_model, service_model
from pprint import pprint
import json


def main():
    mongo_manager.setup()
    p = initiate_user("test")


def engine():
    mongo_manager.setup_orm()
    p = person_model.Person(username="test")
    p.google_service.authenticate("GoogleToken")
    p.save()


if __name__ == '__main__':
    # main()
    engine()
