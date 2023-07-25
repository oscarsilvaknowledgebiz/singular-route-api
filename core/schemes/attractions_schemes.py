from typing import Optional
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null


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
    attraction_main_attraction: bool = Field(default=True)
    attraction_sub_attractions_id: Optional[str] = Field(default=null, alias="Id of Attractions that are part of this event")
    attraction_smoke_free: Optional[bool] = Field(default=False, alias="Is the attraction smokers free")
    attraction_children_free: Optional[bool] = Field(default=False, alias="Is this attraction adult only")
    attraction_available_parking: Optional[bool] = Field(default=False, alias="Does the attraction have available parking")
    attraction_pet_friendly: Optional[bool] = Field(default=False, alias="Is this attraction pet friendly")


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
