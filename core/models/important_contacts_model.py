from mongoengine import Document, ObjectIdField, StringField


class ImportantContacts(Document):
    """
    important contacts model database
    """
    _id = ObjectIdField()
    contact_name = StringField()
    contact_email = StringField()
    contact_phone = StringField()
    contact_type = StringField()