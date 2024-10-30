import time
from src.domain.models.group import Group
from src.domain.use_cases.groups.group_list import GroupList as GroupListInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterfaces
from src.data.erros.domain_errors import BadRequestError, InternalServerError
from src.data.use_cases.relations.validate import ValidateInterface
from src.data.use_cases.groups.group_join import GroupJoinInterface


class GroupList(GroupListInterface):

    def __init__(self, users_groups: UserGroupInterfaces,
                 validate: ValidateInterface,
                 group_join: GroupJoinInterface) -> None:
        self.__users_groups = users_groups
        self.__validate = validate
        self.__group_join = group_join

    def list(self, token: str) -> list[Group]:
        try:
            user = self.__validate.user_token(token=token)
            groups_entitys = self.__users_groups.select_user_relations(user.email)
            if len(groups_entitys) <= 0:
                self.__group_join.join(token=token, group_id="0")
                groups_entitys = self.__users_groups.select_user_relations(user.email)
            groups = [Group(group_id=group.group_id, title=group.title).to_dict()
                      for group in groups_entitys]
            return groups
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e
