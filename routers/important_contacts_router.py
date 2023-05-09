from fastapi import APIRouter, Response, status
import core.schemes
import database.important_contacts_database

router = APIRouter()


@router.post("/by-id/{id_user}",
             summary="Creates a new important contact",
             description="Creates a new important contact",
             response_description="Creates a new important contact",
             response_model=core.schemes.important_contacts_schemes.ImportantContactsCreateResponse,
             operation_id="CreateImportantContact"
             )
async def create_important_contact(important_contact: core.schemes.important_contacts_schemes.ImportantContactsPost):
    response = database.important_contacts_database.add_important_contact(important_contact)
    return {"msg": "success",
            "data": {response}}


@router.get("/",
            summary= "Return important contact",
            description= "Return important contact",
            response_model= core.schemes.important_contacts_schemes.ImportantContactsCreateResponse,
            operation_id="GetImportantContact"
            )
async def service(response: Response):
    response_database = database.important_contacts_database.return_important_contacts()
    if response_database is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "error", "data": "This User does not exist"}
    else:
        return {"msg": "success",
            "data": response_database}
