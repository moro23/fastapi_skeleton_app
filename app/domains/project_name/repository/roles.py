from crud.base import CRUDBase
from domains.project_name.models.roles_permissions import Role
from domains.project_name.schemas.roles import (
    RoleCreate, RoleUpdate
)


class CRUDRole(CRUDBase[Role, RoleCreate, RoleUpdate]):
    pass
role_actions = CRUDRole(Role)