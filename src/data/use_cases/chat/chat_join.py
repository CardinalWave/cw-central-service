from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.use_cases.chat.chat_join import ChatJoin as ChatJoinInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface
from src.domain.use_cases.relations.user_status import UserStatus as UserStatusInterface
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.infra.security.implementations.secure_email import SecureEmailInterface
from src.domain.enums.UserStatusType import UserStatusType


class ChatJoin(ChatJoinInterface):

    def __init__(self, user_group: UserGroupInterface,
                 user_status: UserStatusInterface,
                 forward_message: ForwardMessageInterface,
                 user_repository: UsersRepositoryInterface,
                 secure_email: SecureEmailInterface):
        self.__user_group = user_group
        self.__user_status = user_status
        self.__forward_message = forward_message
        self.__user_repository = user_repository
        self.__secure_email = secure_email

    def join(self, group: Group, email: str) -> Dict:
        secure_email = self.__validate_email(email)
        user = self.__search_user(email)
        user_status = self.__user_status.in_group(secure_email=secure_email, group=group)
        if user_status == UserStatusType.IN_GROUP:
            self.__forward_message.join_group(user=user, group=group)

    def __search_user(self, email) -> User:
        user_entity = self.__user_repository.select_email(email)
        return User(token=user_entity.token, email=user_entity.email,
                    username=user_entity.username)

    def __validate_email(self, email: str) -> str:
        return self.__validate_email(email)