from mongoengine import Document, ObjectIdField, StringField, BooleanField, EmbeddedDocumentField, EmbeddedDocument


class Wishlist(Document):
    """
    User model database
    """
    _id = ObjectIdField()
    from mongoengine import Document, ObjectIdField, StringField, BooleanField, EmbeddedDocumentField, EmbeddedDocument

    class Wishlist(Document):
        """
        User model database
        """
        _id = ObjectIdField()
        wishlist_id_user = StringField()
        wishlist_id_local = StringField()
        wishlist_nome_local = StringField()
        wishlist_date_added = StringField()

