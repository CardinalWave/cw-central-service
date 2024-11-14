#pylint: disable=inconsistent-return-statements
import json
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.session import Session
from src.domain.use_cases.chat.chat_join import ChatJoin as ChatJoinInterface
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError, NotFoundError
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface
from src.main.logs.logs_interface import LogInterface

class ChatJoin(ChatJoinInterface):

    def __init__(self,
                 forward_message: ForwardMessageInterface,
                 validate: ValidateInterface,
                 user_group: UserGroupInterface,
                 logger: LogInterface):

        self.__forward_message = forward_message
        self.__validate = validate
        self.__user_group = user_group
        self.__logger = logger

    def join(self, group_id: str, token: str) -> Dict:
        try:
            user, session = self.__validate_user(token=token)
            group = self.__validate_group(group_id=group_id, email=user.email)
            self.__send_message(session=session, group_id=group.group_id, username=user.username)
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def __validate_user(self, token: str) -> tuple:
        try:
            user, session = self.__validate.user_session_token(token)
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

    def __send_message(self, session: Session, group_id: str, username: str):
        try:
            params = json.dumps({
                        "session_id": session.session_id,
                        "group_id": group_id,
                        "device": session.device,
                        "username": username
                    })
            self.__logger.log_session(session=params, action="chat_join")
            self.__forward_message.send_message(params=params, action="/chat/join")
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
