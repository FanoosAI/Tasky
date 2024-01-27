import logging

from opsdroid.skill import Skill
from opsdroid.matchers import match_parse

import mongo_manager


class TestSkill(Skill):
    @match_parse("test")
    async def test_event(self, event):
        print("\n---TEST---\n")

        response = "all people defined in the database: \n"
        people = mongo_manager.get_people()
        response += "\n".join([person[0] + "->" + person[1] for person in people])

        await event.respond(response)
