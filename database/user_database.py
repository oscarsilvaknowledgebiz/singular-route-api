from mongoengine import connect
import core.models as model
import json


CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/singular-route?retryWrites=true&w=majority'


def add_user(value):
    """
    Create new user in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)
    response = model.user_model.User(
        name = value.name,
        email = value.email,
        receives_notification = value.receives_notification,
        notification_email = value.notification_email,
        password = value.password,
        picture = value.picture,
        phone = value.phone,
        birth_date = value.birth_date,
        gmail_access_token = value.gmail_access_token,
        exponent_push_token = value.exponent_push_token
    ).save()
    return str(response[0].auto_id_0)


def return_user_by_email_and_password(email, password):
    connect(host=CONNECTION)
    response = model.user_model.User.objects(email = email, password = password).first()
    response = json.loads(response.to_json()) if response is not None else None
    return response
