from typing import Dict
from src.domain.models.user import User
from src.domain.use_cases.groups.group_join import GroupJoin as GroupJoinInterface
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface
from src.domain.models.users_groups import UsersGroups
from src.domain.models.group import Group
from src.data.erros.domain_errors import BadRequestError, InternalServerError

class GroupJoin(GroupJoinInterface):

    def __init__(self, group_repository: GroupsRepositoryInterface, users_groups: UserGroupInterface) -> None:
        self.__group_repository = group_repository
        self.__users_groups = users_groups
    
    def join(self, user: User, group: Group) -> Dict:
        try:
            finded_group = self.__search_group(group.title)
            self.__search_member(user.email, finded_group.title)
            user_group = self.__register_member(user, finded_group)
            return user_group
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e
        
    def join_global(self, user: User) -> Dict:
        global_group = self.__search_group("GLOBAL")
        user_group = self.join(user, global_group)
        return user_group

    def __search_group(self, title: str) -> Group:
        group_repo = self.__group_repository.select_title(title=title)
        group = Group(group_id=group_repo.id, title=group_repo.title)
        return group

    def __search_member(self, email: str, title: str) -> None:
        groups = self.__users_groups.select_user_relations(secure_email=email)
        for group in groups:
            if group.title == title:
                raise BadRequestError("Usuario ja relacionado ao grupo")

    def __register_member(self, user: User, group: Group) -> UsersGroups:
        return self.__users_groups.join_user(user, group)
