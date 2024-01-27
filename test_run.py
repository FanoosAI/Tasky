import mongo_manager
from mongo_manager.people_manager import *
from models import person_model, service_model
from pprint import pprint
import json


def main():
    mongo_manager.setup()
    p = initiate_user("test")
    pprint(p.__dict__)
    mongo_manager.db["people"].insert_one(json.dumps(p))


if __name__ == '__main__':
    # main()
    s = service_model.OdooService()
    # s = service_model.Service()
    print(s.reprJSON())
