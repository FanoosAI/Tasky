import pprint
import logging
from opsdroid.skill import Skill
from opsdroid.matchers import match_rasanlu


class RasaCalendar(Skill):
    @match_rasanlu('add_event')
    async def add_event(self, message):
        rasa_stuff = message.rasanlu
        logging.info(f'Rasa stuff: {rasa_stuff["intent"]["name"]}')
        pprint.pprint(rasa_stuff)
