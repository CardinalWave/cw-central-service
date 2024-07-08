from src.domain.enums.UserStatusType import UserStatusType
from src.domain.models.group import Group
from src.domain.use_cases.relations.user_status import UserStatus as UserStatusInterface


class UserStatusSpy(UserStatusInterface):

    @classmethod
    def receiver_status(cls, secure_email) -> UserStatusType:
        if secure_email == "test2@outlook.com":
            return UserStatusType.ONLINE
        return UserStatusType.OFFLINE

    @classmethod
    def in_group(cls, secure_email, group: Group) -> UserStatusType:
        if secure_email == "test2@outlook.com":
            return UserStatusType.IN_GROUP
        return UserStatusType.OUT_GROUP

    @classmethod
    def update_status(cls, secure_email):
        pass
