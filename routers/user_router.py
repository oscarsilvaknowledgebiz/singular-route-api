from fastapi import APIRouter
import core.schemes

router = APIRouter()


@router.post("by-id/{id_user}",
             summary="Creates a new user by id_user",
             description="Creates a new user by id_user",
             response_description="Creates a new user",
             response_model=core.schemes.user_schemes.UserCreateResponse,
             operation_id="CreateUserByIdUser"
             )
async def create_user(user: core.schemes.user_schemes.UserPost):
    return {"msg": "success", "data": {}}