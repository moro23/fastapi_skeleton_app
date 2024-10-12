from domains.project_name.apis.roles_permissions import roles_permissions_router
from domains.project_name.apis.permissions import permissions_router
from domains.project_name.apis.roles import roles_router

from domains.auth.apis.logout import logout_auth_router
from domains.auth.apis.email_router import email_router
from domains.auth.apis.users import users_router
from domains.auth.apis.login import auth_router

from fastapi import APIRouter


router = APIRouter()
router.include_router(email_router)
router.include_router(auth_router)
router.include_router(logout_auth_router)
router.include_router(users_router)
router.include_router(roles_permissions_router)
router.include_router(roles_router)
router.include_router(permissions_router)


