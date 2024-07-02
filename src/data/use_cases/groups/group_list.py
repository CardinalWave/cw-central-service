from typing import List
from src.domain.models.user import User
from src.domain.models.group import Group
from src.domain.use_cases.groups.group_list import GroupList as GroupListInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterfaces
from src.data.erros.domain_errors import BadRequestError, InternalServerError


class GroupList(GroupListInterface):

    def __init__(self, users_groups: UserGroupInterfaces) -> None:
        self.__users_groups = users_groups

    def list(self, user: User) -> List[Group]:
        try:
            groups_entitys = self.__users_groups.select_user_relations(user.email)
            groups = [Group(group_id=group.group_id, title=group.title).to_dict() for group in groups_entitys]
            return groups
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e
