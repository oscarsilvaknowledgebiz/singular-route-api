from mongoengine import Document, ObjectIdField, StringField


class News(Document):
    """
    News model database
    """
    _id = ObjectIdField()
    news_event_type = StringField()
    news_state = StringField()
    news_date_time = StringField()
    news_description = StringField()
    news_local = StringField()
