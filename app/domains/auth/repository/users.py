from crud.base import CRUDBase
from domains.auth.models.users import User
from domains.auth.schemas.users import (
    UserCreate, UserUpdate
)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass
user_actions = CRUDUser(User)