from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.history_database

router = APIRouter()


@router.post("/by-id/",
             summary="Creates history",
             description="Creates history",
             response_description="Creates history",
             response_model=core.schemes.history_schemes.HistoryCreateResponse,
             operation_id="Creates history"
             )
async def create_history(history: core.schemes.history_schemes.HistoryPost):
    response = database.history_database.add_history(history)
    return {"msg": "success",
            "data": {response}}


@router.get("/by-id/",
            summary= "Return history",
            description= "Return history",
            response_model= core.schemes.history_schemes.HistoryGetResponse,
            operation_id="GetHistory"
            )
async def service(response: Response):
    response_database = database.history_database.return_history()
    if response_database is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "This User does not exist"}
    else:
        return {"msg": "success",
            "data": response_database}
