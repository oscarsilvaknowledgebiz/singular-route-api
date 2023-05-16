from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.user_database

router = APIRouter()


@router.get("/by-id/{email}",
            summary="Return user data by email to reset password",
            description="Return data of user by email",
            response_model=core.schemes.user_schemes.UserGetResponse,
            operation_id="GetUserDataByIdUser"
            )
async def service(response: Response, email: str):
    response_database = database.user_database.return_user_by_email(email)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "This User does not exist"}
    else:
        return {"msg": "success",
                "data": response_database}

