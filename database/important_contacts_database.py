from mongoengine import connect
import core.models as model
import json
import core.models.important_contacts_model

CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/singular-route?retryWrites=true&w=majority'


def add_important_contact(value):
    """
    Create new important contact in databse
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.important_contacts_model.ImportantContacts(
        contact_name = value.contact_name,
        contact_email = value.contact_email,
        contact_phone = value.contact_phone,
        contact_type = value.contact_type
    ).save()
    return str(response.auto_id_0)


def return_important_contacts():
    connect(host=CONNECTION)
    response = model.important_contacts_model.ImportantContacts.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response
