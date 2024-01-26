from pprint import pprint

from opsdroid.skill import Skill
from opsdroid.matchers import match_catchall, match_event
from opsdroid.events import UserInvite, JoinRoom, LeaveRoom


class AllEventsSkill(Skill):
    @match_catchall
    async def all_events(self, event):
        print("\n---ALWAYS---\n")
        print(f"all events -> {event}")
        if event:
            pprint(vars(event))

    @match_event(UserInvite)
    async def user_invite(self, invite):
        print("\n---USER INVITE---\n")
        print(f"user invite -> {invite}")
        pprint(vars(invite))
        if isinstance(invite, UserInvite):
            await invite.respond(JoinRoom())

    @match_event(LeaveRoom)
    async def user_leave(self, leave):
        print("\n---USER LEAVE---\n")
        print(f"user leave -> {leave}")
        pprint(vars(leave))
        if isinstance(leave, LeaveRoom):
            await leave.respond("I'm leaving!")