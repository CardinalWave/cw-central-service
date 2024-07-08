import datetime as dt
from typing import Dict
from src.domain.models.message import Message
from src.domain.use_cases.chat.chat_send import ChatSend as ChatSendInterface
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.data.erros.domain_errors import NotFoundError, BadRequestError
from src.domain.models.user import User
from src.domain.models.group import Group
from src.domain.models.session import Session
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface


class ChatSend(ChatSendInterface):

    def __init__(self, validate: ValidateInterface,
                 forward_message: ForwardMessageInterface):
        self.__validate = validate
        self.__forward_message = forward_message

    def send(self, token: str, group_id: str, message: str) -> Dict:
        user, session = self.__validate_user(token=token)
        group = self.__validate_group(group_id=group_id, email=user.email)
        message_payload = self.__send_message(user, group, session, message)
        return message_payload.to_dict()

    def __validate_user(self, token: str) -> tuple:
        try:
            user, session = self.__validate.user_session_token(token=token)
            return user, session
        except NotFoundError as e:
            raise NotFoundError(str(e)) from e

    def __validate_group(self, group_id: str, email: str) -> Group:
        try:
            group = self.__validate.group_id(group_id=group_id, email=email)
            return group
        except NotFoundError as e:
            raise NotFoundError(str(e)) from e

    def __send_message(self, user: User, group: Group, session: Session, message: str) -> Message:
        try:
            current_time = dt.datetime.now()
            message_payload = Message(group_id=group.group_id,
                                      session=session,
                                      username=user.username,
                                      payload=message,
                                      action="send",
                                      send_time=current_time)
            self.__forward_message.send_message(user=user,
                                                group=group,
                                                session=session,
                                                action="send",
                                                message=message_payload.to_dict())

            return message_payload
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
