from mongoengine import Document, ObjectIdField, StringField, BooleanField, EmbeddedDocumentField, EmbeddedDocument


class Restaurants(Document):
    """
    Restaurant model database
    """
    _id = ObjectIdField()
    restaurant_name = StringField()
    restaurant_schedule = StringField()
    restaurant_rating = StringField()
    restaurant_average_price = StringField()
    restaurant_email = StringField()
    restaurant_phone = StringField()
    restaurant_menu_link = StringField()
    restaurant_capacity = StringField()
    restaurant_pictures = StringField()
    restaurant_type = StringField()
    restaurant_additional_information = StringField()
    restaurant_personal_notes = StringField()