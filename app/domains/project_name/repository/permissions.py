from crud.base import CRUDBase
from domains.project_name.models.role_permissions import Permission
from domains.project_name.schemas.permissions import (
    PermissionCreate, PermissionUpdate
)


class CRUDRole(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    pass
perm_actions = CRUDRole(Permission)