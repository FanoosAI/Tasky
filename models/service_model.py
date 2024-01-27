import transitions


class Service:
    states = ['UnAuthenticated', 'Ready', 'PendingRequest', ]

    def __init__(self, states=None):
        if states is not None:
            states = Service.states
        self.machine = transitions.Machine(model=self, states=states, initial='UnAuthenticated')

        self.machine.add_transition('authenticated', 'UnAuthenticated', 'Ready')
        self.machine.add_transition('requested', 'Ready', 'PendingRequest')
        self.machine.add_transition('finished_request', 'PendingRequest', 'Ready')

    def reprJSON(self):
        return dict(service_type=self.__class__.__name__, state=self.state)


class GoogleCalendarService(Service):

    def __init__(self):
        super().__init__()
        self.token = None

    def authenticate(self, token):
        self.token = token
        self.authenticated()

    def reprJSON(self):
        d = super().reprJSON()
        d.update({
            "token": self.token
        })
        return d


class OdooService(Service):
    pass
