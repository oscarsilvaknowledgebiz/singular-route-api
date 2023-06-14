from pydantic import BaseModel


class ImportantContactsPost(BaseModel):
    """
    Contacts Post
    """
    contact_name: str
    contact_phone: str
    contact_email: str
    contact_type: str


class ImportantContactsCreateResponse(BaseModel):
    """
    Contacts create response
    """
    msg: str
    data: list
