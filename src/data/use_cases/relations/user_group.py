#pylint: disable=line-too-long
import datetime as dt
from uuid import uuid4
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.users_groups import UsersGroups
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInteface
from src.infra.db.interfaces.users_groups_repository import UsersGroupsRepositoryInterface
from src.infra.security.interfaces.secure_email import SecureEmailInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError


class UserGroup(UserGroupInteface):
    def __init__(self, users_groups_repository: UsersGroupsRepositoryInterface,
                 secure_email: SecureEmailInterface) -> None:
        self.__users_groups_repository = users_groups_repository
        self.__secure_email = secure_email

    def join_user(self, user: User, group: Group) -> Dict:
        try:
            users_groups_id = str(uuid4())
            encrypt_email = self.__secure_email.encrypt_email(user.email)
            updated_at = dt.datetime.now()
            self.__users_groups_repository.join_user(id=users_groups_id,
                                                     secure_email=encrypt_email,
                                                     user_token=user.token,
                                                     username=user.username,
                                                     group_title=group.title,
                                                     group_id=group.group_id,
                                                     updated_at=updated_at)

            user_group = UsersGroups(id=users_groups_id,
                                     secure_email=encrypt_email,
                                     group_title=group.title,
                                     group_id=group.group_id,
                                     updated_at=str(updated_at))

            return user_group.to_dict()
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def select_user_relations(self, email: str) -> list[Group]:
        try:
            print(email)
            groups = []
            encrypt_email = self.__secure_email.encrypt_email(email=email)
            users_group_entitys = self.__users_groups_repository.select_user_relations(secure_email=encrypt_email)
            if len(users_group_entitys) > 0:
                groups = [Group(group_id=relations.group_id, title=relations.group_title) for relations in
                          users_group_entitys]
            return groups

        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def select_group_relations(self, group_id: str) -> list[User]:
        try:
            users_group_entitys = self.__users_groups_repository.select_group_relations(group_id=group_id)
            users = [User(token=users.user_token, email=users.secure_email, username=users.username) for users in
                     users_group_entitys]
            return users
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def update_relation(self, user: User, group: Group) -> Dict:
        try:
            datetime = dt.datetime.now()
            encrypt_email = self.__secure_email.encrypt_email(user.email)
            users_groups_entity = self.__users_groups_repository.update_relation(
                secure_email=encrypt_email,
                group_id=group.group_id,
                updated_at=datetime)

            users_groups = UsersGroups(id=users_groups_entity.id,
                                       secure_email=users_groups_entity.secure_email,
                                       group_title=users_groups_entity.group_title,
                                       group_id=users_groups_entity.group_id,
                                       updated_at=users_groups_entity.updated_at)
            return users_groups.to_dict()
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e
