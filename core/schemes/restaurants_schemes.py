from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class RestaurantPost(BaseModel):
    """
    Restaurant
    Post
    """
    _id: str
    restaurant_name: str
    restaurant_schedule: str
    restaurant_rating: Optional[str] = Field(default=null, alias="Restaurant User Rating")
    restaurant_average_price: str
    restaurant_email: Optional[str] = Field(default=null, alias="Restaurant EMail")
    restaurant_phone: Optional[str] = Field(default=null, alias="Restaurant Phone")
    restaurant_menu_link: str
    restaurant_capacity: str
    restaurant_pictures: Optional[str] = Field(default=null, alias="Restaurant Pictures")
    restaurant_type: Optional[str] = Field(default=null, alias="Restaurant Type")
    restaurant_additional_information: Optional[str] = Field(default=null, alias="Additional Info")
    restaurant_personal_notes: Optional[str] = Field(default=null, alias="Personal Notes")
    restaurant_pet_friendly: bool
    restaurant_no_smokers: bool


class RestaurantCreateResponse(BaseModel):
    """
    Restaurant create response
    """
    msg: str
    data: object = {}


class RestaurantGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
    data: object = {}

