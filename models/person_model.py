from models.service_model import GoogleCalendarService, OdooService
from mongoengine import Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ListField, DictField, \
    EmbeddedDocumentListField


class Person(Document):
    username = StringField(required=True, unique=True)
    google_service = EmbeddedDocumentField(GoogleCalendarService)
    odoo_service = EmbeddedDocumentField(OdooService)

    meta = {
        'collection': 'people'
    }

    def __init__(self, username: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.id:
            # This line checks if the object is being created for the first time or if it is being loaded from the DB.
            return

        self.username = username
        if not self.google_service:
            self.google_service = GoogleCalendarService()
        if not self.odoo_service:
            self.odoo_service = OdooService()

    def __str__(self):
        return f"Person: {self.username}"
