from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.session import Session
from src.domain.use_cases.chat.chat_join import ChatJoin as ChatJoinInterface
from src.domain.use_cases.relations.user_status import UserStatus as UserStatusInterface
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.infra.security.implementations.secure_email import SecureEmailInterface
from src.domain.enums.UserStatusType import UserStatusType
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError, NotFoundError


class ChatJoin(ChatJoinInterface):

    def __init__(self,
                 forward_message: ForwardMessageInterface,
                 user_repository: UsersRepositoryInterface,
                 secure_email: SecureEmailInterface,
                 validate: ValidateInterface,
                 user_status: UserStatusInterface):

        self.__forward_message = forward_message
        self.__user_repository = user_repository
        self.__secure_email = secure_email
        self.__validate = validate
        self.__user_status = user_status

    def join(self, group_id: str, token: str) -> Dict:
        try:
            group = self.__search_group(group_id=group_id)
            user, session = self.__search_user(user_token=token)
            print(user.email)
            user_status = self.__user_status.in_group(email=user.email, group=group)
            print(user_status)
            if user_status == UserStatusType.IN_GROUP:
                self.__forward_message.send_message(user=user,
                                                    group=group,
                                                    session=session,
                                                    action="join",
                                                    message=group.to_dict())
                print(group)
                return group.to_dict()
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def __search_user(self, user_token: str) -> tuple:
        try:
            user_entity = self.__user_repository.select_token(user_token)
            if user_entity.token == user_token:
                user = User(token=user_entity.token,
                     email=user_entity.email,
                     username=user_entity.username)
                session = Session(session_id=user_entity.session_id,
                        device=user_entity.device)
                return user, session
        except NotFoundError as e:
            raise NotFoundError("Usuario nao encontrado!") from e


    def __search_group(self, group_id) -> Group:
        try:
            group = self.__validate.group_id(group_id=group_id)
            return group
        except NotFoundError as e:
            raise NotFoundError("Grupo nao encontrado") from e