import pprint
import logging
from opsdroid.skill import Skill
from opsdroid.matchers import match_rasanlu
import googleAPI
from opsdroid.helper import get_opsdroid


class RasaCalendar(Skill):
    @match_rasanlu('farsi_add_event')
    async def add_event(self, message):
        rasa_stuff = message.rasanlu
        logging.info(f'Rasa stuff: {rasa_stuff["intent"]["name"]}')
        pprint.pprint(rasa_stuff)
        print("\n===============================\n")
        print(get_opsdroid().config)
        entities = {i['entity']: i['value'] for i in rasa_stuff['entities']}
        # pprint.pprint(entities)
        print("\n===============================\n")
        await message.respond(f"entities: {entities}")

    @match_rasanlu('farsi_get_event')
    async def get_events(self, message):
        rasa_stuff = message.rasanlu
        logging.info(f'Rasa stuff: {rasa_stuff["intent"]["name"]}')
        pprint.pprint(rasa_stuff)
        print("\n===============================\n")
        entities = {i['entity']: i['value'] for i in rasa_stuff['entities']}
        pprint.pprint(entities)
        print("\n===============================\n")

        persian_response_text = "نمایش رویداد‌ها"
        if "date" in entities:
            persian_response_text += "برای تاریخ: " + entities["date"]

        persian_response_text += "\n TODO"
        await message.respond(persian_response_text)

    @match_rasanlu('authorize_google')
    async def authorize_google(self, message):
        rasa_stuff = message.rasanlu
        logging.info(f'Rasa authorize google')
        persian_response_text = "برای  احراز هویت گوگل از لینک زیر استفاده کنید\n"
        persian_response_text += googleAPI.init_url()
        await message.respond(persian_response_text)
