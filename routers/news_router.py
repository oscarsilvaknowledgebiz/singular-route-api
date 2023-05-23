from fastapi import APIRouter, Response, status
import core.schemes
import database.news_database

router = APIRouter()


@router.post("/by-id/{id_user}",
             summary="Creates a new",
             description="Creates a new",
             response_description="Creates a new",
             response_model=core.schemes.news_schemes.NewsCreateResponse,
             operation_id="CreateNew"
             )
async def create_new(new: core.schemes.news_schemes.NewsPost):
    response = database.news_database.add_news(new)
    return {"msg": "success",
            "data": {response}}


@router.get("/by-id/",
            summary="Return news",
            description="Return news",
            response_model=core.schemes.news_schemes.NewsGetResponse,
            operation_id="GetUserDataByIdUser"
            )
async def service(response: Response):
    response_database = database.news_database.return_news()
    if response_database is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "error", "data": "This User does not exist"}
    else:
        return {"msg": "success",
                "data": response_database}
