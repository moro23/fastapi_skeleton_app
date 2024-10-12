from typing import List, Any

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.base_class import UUID
from domains.auth.repository.users import user_actions 
from domains.auth.schemas.users import UserSchema, UserCreate, UserUpdate


class UserService:


    def list_users(self, *, db: Session, skip: int = 0, limit: int = 100) -> List[UserSchema]:
        users_list = user_actions.get_all(db=db, skip=skip, limit=limit)
        return users_list

    def create_user(self, db: Session, user_in: UserCreate) -> UserSchema:
        #check for duplicate email entries in staff table
        # check_email = db.query(User).filter(User.email ==staff.email).first()
        # if check_email:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email already exist")
        created_user = user_actions.create(db=db, obj_in=user_in)
        return created_user

    def update_user(self, *, db: Session, id: UUID, users_form: UserUpdate) -> UserSchema:
        ## get user by id 
        user = user_actions.get(db=db, id=id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users_form not found")
        updated_user = user_actions.update(db=db, db_obj=users_form_, obj_in=users_form)
        return updated_user

    def get_user_by_id(self, *, db: Session, id: UUID) -> UserSchema:
        ## get user by id 
        user = user_actions.get(db=db, id=id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users_form not found")
        return user

    def delete_user(self, *, db: Session, id: UUID) -> UserSchema:
        ## get user by id 
        user = user_actions.get(db=db, id=id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users_form not found")
        deleted_user = user_actions.remove(db=db, id=id)
        return deleted_user

    # def get_users_by_id(self, *, id: UUID) -> UserSchema:
    #     users_form = user_actions.get(id)
    #     if not users_form:
    #         raise HTTPException(
    #             status_code=status.HTTP_403_FORBIDDEN,
    #             detail="users_form not found"
    #         )
    #     return users_form

    # def get_users_by_keywords(self, *, db: Session, tag: str) -> List[UserSchema]:
    #     pass

    # def search_users(self, *, db: Session, search: str, value: str) -> List[UserSchema]:
    #     pass

    # def read_by_kwargs(self, *, db: Session, **kwargs) -> Any:
    #     return users_form_repo.get_by_kwargs(self, db, kwargs)


user_services = UserService()