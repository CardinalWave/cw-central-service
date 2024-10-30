#pylint: disable=inconsistent-return-statements
import json
from src.domain.use_cases.chat.chat_send import ChatSend as ChatSendInterface
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.data.erros.domain_errors import NotFoundError, BadRequestError
from src.domain.models.group import Group
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface
from src.main.logs.logs_interface import LogInterface


class ChatSend(ChatSendInterface):

    def __init__(self, validate: ValidateInterface,
                 forward_message: ForwardMessageInterface,
                 user_group: UserGroupInterface,
                 logger: LogInterface):
        self.__validate = validate
        self.__forward_message = forward_message
        self.__user_group = user_group
        self.__logger = logger

    def send(self, token: str, group_id: str, message: str):
        user, session = self.__validate_user(token=token)
        self.__validate_group(group_id=group_id, email=user.email)
        self.__send_message(session_id=session.session_id, message=message)

    def __validate_user(self, token: str) -> tuple:
        try:
            user, session = self.__validate.user_session_token(token=token)
            return user, session
        except NotFoundError as e:
            raise NotFoundError(str(e)) from e

    def __validate_group(self, group_id: str, email: str) -> Group:
        try:
            list_group = self.__user_group.select_user_relations(email)
            for group in list_group:
                if group.group_id == group_id:
                    return group
        except NotFoundError as e:
            raise NotFoundError(str(e)) from e

    def __send_message(self, session_id: str, message: str):
        try:
            params = json.dumps({
                "session_id": session_id,
                "payload": message
            })
            self.__logger.log_session(session=params, action="chat_join")
            self.__forward_message.send_message(params=params, action="/chat/send")
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
