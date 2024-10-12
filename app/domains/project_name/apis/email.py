from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND





from db.session import get_db



# APIRouter creates path operations for admin and users module
email_service_router = APIRouter(
    prefix="/perms",
    tags=["Email Service"],
    responses={404: {"description": "Not found"}},
)

@email_service_router.post("send_email")