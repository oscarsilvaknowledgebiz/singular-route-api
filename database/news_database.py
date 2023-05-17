from mongoengine import connect
import core.models as model
import json

CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/singular-route?retryWrites=true&w=majority'


def add_news(value):
    """
    Creates a new in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.news_model.News(
        news_event_type=value.news_event_type,
        news_state=value.news_state,
        news_date_time=value.news_date_time,
        news_description=value.news_description,
        news_local=value.news_local
    ).save()
    return str(response.auto_id_0)


def return_news():
    connect(host=CONNECTION)
    response = model.news_model.News.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response
