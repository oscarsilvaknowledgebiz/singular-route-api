from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class HistoryPost(BaseModel):
    """
    User Post
    """
    _id: str
    history_id_user: str
    history_id_local:str
    history_local_name: str
    history_date_last_visit: str


class HistoryCreateResponse(BaseModel):
    """
    User create response
    """
    msg: str
    data: object = {}


class HistoryGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
    data: object = {}

