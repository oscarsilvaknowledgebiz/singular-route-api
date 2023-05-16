from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.wishlist_database

router = APIRouter()


@router.post("/by-id",
             summary="Creates a new wishlist",
             description="Creates a new wishlist",
             response_description="Creates a new wishlist",
             response_model=core.schemes.wishlist_schemes.WishlistCreateResponse,
             operation_id="CreateWishlist"
             )
async def create_wishlist(wishlist: core.schemes.wishlist_schemes.WishlistPost):
    response = database.wishlist_database.add_wishlist(wishlist)
    return {"msg": "success",
            "data": {response}}


@router.get("/by-id",
            summary="Return wishlist",
            description="Return wishlist",
            response_model=core.schemes.wishlist_schemes.WishlistGetResponse,
            operation_id="GetWishlist"
            )
async def service(response: Response):
    response_database = database.wishlist_database.return_wishlist()
    if response_database is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "This does not exist"}
    else:
        return {"msg": "success",
                "data": response_database}
