from mongoengine import Document, ObjectIdField, StringField, BooleanField

class User(Document):
    """
    User model database
    """
    _id = ObjectIdField()
    name = StringField()
    email = StringField()
    receives_notification = BooleanField()
    notification_email = StringField()
    password = StringField()
    picture = StringField()
    phone = StringField()
    birth_date = StringField()
    gmail_access_token = StringField()
    exponent_push_token = StringField()