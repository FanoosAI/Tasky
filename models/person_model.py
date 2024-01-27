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

    def __init__(self, username: str):
        super().__init__()
        self.username = username
        self.google_service = GoogleCalendarService()
        self.odoo_service = OdooService()

    def __str__(self):
        return f"Person: {self.username}"
