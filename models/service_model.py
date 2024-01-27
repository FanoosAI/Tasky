import transitions
import mongoengine


class Service(mongoengine.EmbeddedDocument):
    states = ['UnAuthenticated', 'Ready', 'PendingRequest', ]
    state = mongoengine.StringField(required=True)

    def __init__(self, states=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if states is None:
            states = Service.states
        self.machine = transitions.Machine(model=self, states=states, initial=states[0])

        self.machine.add_transition('authenticated', 'UnAuthenticated', 'Ready')
        self.machine.add_transition('requested', 'Ready', 'PendingRequest')
        self.machine.add_transition('finished_request', 'PendingRequest', 'Ready')

    meta = {
        'allow_inheritance': True
    }

    def __str__(self):
        return f"Service: {self.state}"


class GoogleCalendarService(Service):
    token = mongoengine.StringField(required=False)

    def authenticate(self, token):
        self.token = token
        self.authenticated()

    def __str__(self):
        return f"GoogleCalendarService: {self.state}"


class OdooService(Service):
    pass
