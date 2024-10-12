from crud.base import CRUDBase
from domains.project_name.models.roles_permissions import role_permissions
from domains.project_name.schemas.roles_permissions import (
   RolePermissionBase, RolePermissionCreate, RolePermissionUpdate

)


class CRUDRole(CRUDBase[role_permissions, RolePermissionCreate, RolePermissionUpdate]):
    pass
role_perm_actions = CRUDRole(role_permissions)