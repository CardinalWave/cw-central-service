from typing import Dict
from src.domain.models.user import User
from src.domain.use_cases.groups.group_join import GroupJoin as GroupJoinInterface
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.domain.models.group import Group
from src.data.erros.domain_errors import BadRequestError, InternalServerError


class GroupJoin(GroupJoinInterface):

    def __init__(self,
                 group_repository: GroupsRepositoryInterface,
                 users_groups: UserGroupInterface,
                 validate: ValidateInterface) -> None:

        self.__group_repository = group_repository
        self.__users_groups = users_groups
        self.__validate = validate

    def join(self, token: str, group_id: str) -> Dict:
        try:
            user = self.__validate.user_token(token)
            found_group = self.__search_group(group_id=group_id)
            self.__search_member(email=user.email, title=found_group.title)
            user_group = self.__register_member(user, found_group)
            return user_group
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def __search_group(self, group_id: str) -> Group:
        group_repo = self.__group_repository.select_group_id(group_id=group_id)
        group = Group(group_id=group_repo.id, title=group_repo.title)
        return group

    def __search_member(self, email: str, title: str) -> None:
        groups = self.__users_groups.select_user_relations(email=email)

        for group in groups:
            if group.title == title:
                raise BadRequestError("Usuario ja relacionado ao grupo")

    def __register_member(self, user: User, group: Group) -> Dict:
        return self.__users_groups.join_user(user, group)
