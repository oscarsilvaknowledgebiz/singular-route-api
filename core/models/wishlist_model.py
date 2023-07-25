from mongoengine import Document, ObjectIdField, StringField


class Wishlist(Document):
    """
    User model database
    """
    _id = ObjectIdField()

    class Wishlist(Document):
        """
        User model database
        """
        _id = ObjectIdField()
        wishlist_id_user = StringField()
        wishlist_id_local = StringField()
        wishlist_nome_local = StringField()
        wishlist_date_added = StringField()
