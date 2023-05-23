from mongoengine import connect
import core.models as model
import json


CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/singular-route?retryWrites=true&w=majority'


def add_history(value):
    """
    Create new user in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.history_model.History(
        history_id_user=value.history_id_user,
        history_id_local=value.history_id_local,
        history_local_name=value.history_local_name,
        history_date_last_visit=value.history_date_last_visit
    ).save()
    return str(response.auto_id_0)


def return_history():
    connect(host=CONNECTION)
    response = model.history_model.History.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response
