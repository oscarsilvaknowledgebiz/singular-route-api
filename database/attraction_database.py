from mongoengine import connect
import core.models as model
import json

CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/singular-route?retryWrites=true&w=majority'


def add_attraction(value):
    """
    Create a new attraction in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.attraction_model.Attraction(
        attraction_name=value.attraction_name,
        attraction_type=value.attraction_type,
        attraction_location=value.attraction_location,
        attraction_manager_name=value.attraction_manager_name,
        attraction_schedule=value.attraction_schedule,
        attraction_rating=value.attraction_rating,
        attraction_email=value.attraction_email,
        attraction_phone=value.attraction_phone,
        attraction_website=value.attraction_website,
        attraction_price=value.attraction_price,
        attraction_additional_information=value.attraction_additional_information,
        attraction_personal_notes=value.attraction_personal_notes,
        attraction_main_attraction=value.attraction_main_attraction,
        attraction_sub_attractions_id=value.attraction_sub_attractions_id,
        attraction_smoke_free = value.attraction_smoke_free,
        attraction_children_free = value.attraction_children_free,
        attraction_available_parking = value.attraction_available_parking,
        attraction_pet_friendly = value.attraction_pet_friendly
    ).save()
    return str(response.auto_id_0)


def return_attraction():
    connect(host=CONNECTION)
    response = model.attraction_model.Attraction.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response
