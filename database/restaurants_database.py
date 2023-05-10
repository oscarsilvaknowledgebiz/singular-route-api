from mongoengine import connect
import core.models as model
import json

import core.models.restaurants_model

CONNECTION = 'mongodb+srv://basic_user:n1RmcatLryuYJwYY@knowledgebiz-cluster.m8nzdrm.mongodb.net/singular-route?retryWrites=true&w=majority'


def add_restaurant(value):
    """
    Create new restaurant in database
    :param value:
    :return:
    """
    connect(host=CONNECTION)

    response = model.restaurants_model.Restaurants(
        restaurant_name=value.restaurant_name,
        restaurant_schedule=value.restaurant_schedule,
        restaurant_rating=value.restaurant_rating,
        restaurant_average_price=value.restaurant_average_price,
        restaurant_email=value.restaurant_email,
        restaurant_phone=value.restaurant_phone,
        restaurant_menu_link=value.restaurant_menu_link,
        restaurant_capacity=value.restaurant_capacity,
        restaurant_pictures=value.restaurant_pictures,
        restaurant_type=value.restaurant_type,
        restaurant_additional_information=value.restaurant_additional_information,
        restaurant_personal_notes=value.restaurant_personal_notes
    ).save()
    return str(response.auto_id_0)


def return_restaurant(email, password):
    connect(host=CONNECTION)
    response = model.restaurants_model.Restaurants.objects()
    response = json.loads(response.to_json()) if response is not None else None
    return response
