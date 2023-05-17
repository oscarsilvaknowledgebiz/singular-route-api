from mongoengine import connect
import core.models as model
import json
import core.models.wishlist_model

CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/singular-route?retryWrites=true&w=majority'


def add_wishlist(value):
    """
    Create new user in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.wishlist_model.Wishlist(
        wishlist_id_user = value.wishlist_id_user,
        wishlist_id_local = value.wishlist_id_local,
        wishlist_nome_local = value.wishlist_nome_local,
        wishlist_date_added = value.wishlist_date_added
    ).save()
    return str(response.auto_id_0)


def return_wishlist():
    connect(host=CONNECTION)
    response = model.wishlist_model.Wishlist.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response
