from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.restaurants_database

router = APIRouter()


@router.post("/by-id}",
             summary="Creates a new restaurant",
             description="Creates a new restaurant",
             response_description="Creates a new restaurant",
             response_model=core.schemes.restaurants_schemes.RestaurantCreateResponse,
             operation_id="CreateRestaurant"
             )
async def create_restaurant(restaurant: core.schemes.restaurants_schemes.RestaurantPost):
    response = database.restaurants_database.add_restaurant(restaurant)
    return {"msg": "success",
            "data": {response}}


@router.get("/by-id",
            summary="Return user data by email and password",
            description="Return data of user by email and password",
            response_model=core.schemes.restaurants_schemes.RestaurantGetResponse,
            operation_id="GetRestaurant"
            )
async def service(response: Response):
    response_database = database.restaurants_database.return_restaurant
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "This does not exist"}
    else:
        return {"msg": "success",
                "data": response_database}
