from mongoengine import Document, ObjectIdField, StringField


class History(Document):
    """
    User model database
    """
    _id = ObjectIdField()
    history_id_user = StringField()
    history_id_local = StringField()
    history_local_name = StringField()
    history_date_last_visit = StringField()
