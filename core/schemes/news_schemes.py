from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field
from pyasn1.compat.octets import null
from fastapi import Depends


class NewsPost(BaseModel):
    """
    News Post
    """
    _id: str
    news_event_type: str
    news_state: str
    news_date_time: str
    news_description: str
    news_local: str


class NewsCreateResponse(BaseModel):
    """
    News create response
    """
    msg: str
    data: object = {}


class NewsGetResponse(BaseModel):
    """
    News get response scheme
    """
    msg: str
    data: object = {}
