from pydantic import BaseModel


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
