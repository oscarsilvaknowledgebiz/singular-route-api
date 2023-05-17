from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class AttractionPost(BaseModel):
    """
    Attraction Post Model
    """
    _id: str
    attraction_name: str
    attraction_type: str
    attraction_location: str
    attraction_manager_name: str
    attraction_schedule: str
    attraction_rating: Optional[str] = Field(default=null, alias="Attraction User Rating")
    attraction_email: Optional[str] = Field(default=null, alias="Attraction E-Mail Address")
    attraction_phone: Optional[str] = Field(default=null, alias="Attraction Phone Number")
    attraction_website: Optional[str] = Field(default=null, alias="Attraction Website")
    attraction_price: str
    attraction_additional_information: Optional[str] = Field(default=null, alias="Attraction Additional Info")
    attraction_personal_notes: Optional[str] = Field(default=null, alias="Attraction Personal Notes")
    attraction_pet_friendly: bool
    attraction_no_smokers: bool


class AttractionCreateResponse(BaseModel):
    """
    User create response
    """
    msg: str
    data: object = {}


class AttractionGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
