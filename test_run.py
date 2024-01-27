import mongo_manager
from mongo_manager.people_manager import *
from models import person_model, service_model
from pprint import pprint
import json


def main():
    mongo_manager.setup_orm()
    # print(user_exists("ssaaeee@parsi.ai"))
    # person_model.Person.objects.delete()
    # person_model.Person(username="user1").save()
    # person_model.Person(username="user2").save()
    # try:
    #     initiate_user("user1")
    # except exceptions.UserAlreadyExistsException:
    #     print("skipped user initiation")

    # user = get_person('user1')
    # user.google_service.authenticate("token 3:11PM")
    # user.save()
    # print(user.google_service.state)


    user1 = get_person('user1')
    print(user1.google_service.state)


if __name__ == '__main__':
    main()
