from opsdroid.skill import Skill
from opsdroid.matchers import match_rasanlu

from mongo_manager import people_manager


class InitiateSkill(Skill):
    @match_rasanlu('initiate')
    async def initiate(self, message):
        if people_manager.user_exists(message.user):
            await message.respond("شما قبلا ثبت نام کرده‌اید")
            return
        people_manager.initiate_user(message.user)

        await message.respond("ثبت نام شما با موفقیت انجام شد")
