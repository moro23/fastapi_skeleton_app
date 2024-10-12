from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from domains.auth.schemas import users as schemas
from domains.auth.services.users import user_services
from db.session import get_db


users_router = APIRouter(
       prefix="/users",
    tags=["Users Account"],
    responses={404: {"description": "Not found"}},
)





@users_router.get(
    "/all",
    response_model=List[schemas.UserSchema]
)
def list_users(
        db: Session = Depends(get_db),

        skip: int = 0,
        limit: int = 100
) -> Any:
    users_router = user_services.list_users(db=db, skip=skip, limit=limit)
    return users_router


@users_router.post(
    "/",
    response_model=schemas.UserRead,
    status_code=HTTP_201_CREATED
)
async def create_user(
        *, db: Session = Depends(get_db),
        # 
        users: schemas.UserCreate
) -> Any:
    users_router = await user_services.create_user(db,users)
    return users_router


@users_router.put(
    "/{id}",
    response_model=schemas.UserSchema
)
def update_user(
        *, db: Session = Depends(get_db),

        id: UUID4,
        users_forms_in: schemas.UserUpdate,
) -> Any:
    users_router = user_services.get_user_by_id(db=db, id=id)
    if not users_router:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="users_forms_router not found"
        )
    users_router = user_services.update_user(db=db, id=users_router.id, users_form=users_forms_in)
    return users_router


@users_router.get(
    "/{id}",
    response_model=schemas.UserSchema
)
def get_user(
        *, db: Session = Depends(get_db),

        id: UUID4
) -> Any:
    users_router = user_services.get_user(db=db, id=id)
    if not users_router:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="users_forms_router not found"
        )
    return users_router


@users_router.delete(
    "/{id}",
    response_model=schemas.UserSchema
)
def delete_user(
        *, db: Session = Depends(get_db),

        id: UUID4
) -> Any:
    users_forms_router = user_services.get_user(db=db, id=id)
    if not users_forms_router:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="users_forms_router not found"
        )
    users_router = user_services.delete_user(db=db, id=id)
    return users_router