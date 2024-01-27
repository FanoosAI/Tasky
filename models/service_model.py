import transitions
import mongoengine


class Service(mongoengine.EmbeddedDocument):
    states = ['UnAuthenticated', 'Ready', 'PendingRequest', ]
    state = mongoengine.StringField(required=True)

    meta = {
        'allow_inheritance': True
    }

    def __init__(self, states=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not kwargs.get('_created', False):
            # This line checks if the object is being created for the first time or if it is being loaded from the DB.
            return

        if states is None:
            states = Service.states
        self.machine = transitions.Machine(model=self, states=states, initial=states[0])

        self.machine.add_transition('authenticated', 'UnAuthenticated', 'Ready')
        self.machine.add_transition('requested', 'Ready', 'PendingRequest')
        self.machine.add_transition('finished_request', 'PendingRequest', 'Ready')

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
