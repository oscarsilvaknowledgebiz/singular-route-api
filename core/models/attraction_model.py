from mongoengine import Document, ObjectIdField, StringField, BooleanField, EmbeddedDocumentField, EmbeddedDocument


class Attraction(Document):
    """
    User model database
    """
    _id = ObjectIdField()
    attraction_name = StringField()
    attraction_type = StringField()
    attraction_location = StringField()
    attraction_manager_name = StringField()
    attraction_schedule = StringField()
    attraction_rating = StringField()
    attraction_email = StringField()
    attraction_phone = StringField()
    attraction_website = StringField()
    attraction_price = StringField()
    attraction_additional_information = StringField()
    attraction_personal_notes = StringField()
    attraction_main_attraction = BooleanField()
    attraction_sub_attractions_id = StringField()
    attraction_smoke_free = BooleanField()
    attraction_children_free = BooleanField()
    attraction_available_parking = BooleanField()
    attraction_pet_friendly = BooleanField()