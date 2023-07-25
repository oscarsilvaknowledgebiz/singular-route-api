from pydantic import BaseModel


class WishlistPost(BaseModel):
    """
    Wishlist Post
    """
    _id: str
    wishlist_id_user: str
    wishlist_id_local: str
    wishlist_nome_local: str
    wishlist_date_added: str


class WishlistCreateResponse(BaseModel):
    """
    User create response
    """
    msg: str
    data: object = {}


class WishlistGetResponse(BaseModel):
    """
    User get response scheme
    """
    msg: str
    data: object = {}
