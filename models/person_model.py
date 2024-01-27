from models.service_model import GoogleCalendarService, OdooService


class Person:
    def __init__(self, username):
        self.username = username
        self.google_service = GoogleCalendarService()
        self.odoo_service = OdooService()

    def __str__(self):
        return f"{self.username}"

    def reprJSON(self):
        return dict(username=self.username, google_service=self.google_service, odoo_service=self.odoo_service)
