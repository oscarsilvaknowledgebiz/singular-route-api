from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.attraction_database

router = APIRouter()


@router.post("/by-id",
             summary="Creates a new attraction",
             description="Creates a new attraction",
             response_description="Creates a new attraction",
             response_model=core.schemes.attractions_schemes.AttractionCreateResponse,
             operation_id="CreateAttraction"
             )
async def create_attraction(attraction: core.schemes.attractions_schemes.AttractionPost):
    response = database.attraction_database.add_attraction(attraction)
    return {"msg": "success",
            "data": {response}}


@router.get("/by-id/",
            summary="Return attraction",
            description="Return attraction",
            response_model=core.schemes.attractions_schemes.AttractionGetResponse,
            operation_id="GetAttraction"
            )
async def service(response: Response):
    response_database = database.attraction_database.return_attraction()
    if response_database is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "error", "data": "This User does not exist"}
    else:
        return {"msg": "success",
                "data": response_database}
