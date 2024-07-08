from src.domain.enums.UserStatusType import UserStatusType
from src.domain.models.group import Group
from src.domain.use_cases.relations.user_status import UserStatus as UserStatusInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface


class UserStatus(UserStatusInterface):

    def __init__(self, users_groups: UserGroupInterface):
        self.__users_groups = users_groups
        self.__current_status = UserStatusType.OFFLINE

    def receiver_status(self, secure_email) -> UserStatusType:
        return self.__current_status

    def update_status(self, user_status: UserStatusType):
        self.__current_status = user_status

    def in_group(self, email: str, group: Group) -> UserStatusType:
        relations = self.__users_groups.select_user_relations(email=email)
        for relation in relations:
            if relation.group_id == group.group_id or relation.title == group.title:
                return UserStatusType.IN_GROUP
        return UserStatusType.OUT_GROUP
