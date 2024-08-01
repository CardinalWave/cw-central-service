import json
from src.domain.use_cases.chat.chat_leave import ChatLeave as ChatLeaveInterface
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError, NotFoundError
from src.domain.models.session import Session
from src.main.logs.logs import log_session, log_error


class ChatLeave(ChatLeaveInterface):

    def __init__(self,
                 forward_message: ForwardMessageInterface,
                 validate: ValidateInterface):
        self.__forward_message = forward_message
        self.__validate = validate
        self.__user_group = UserGroupInterface

    def leave(self, token: str):
        try:
            session = self.__validate_user(token=token)
            self.__send_message(session)
        except BadRequestError as e:
            log_error(error=e, message=token)
            raise BadRequestError(str(e)) from e
        except Exception as e:
            log_error(error=e, message=token)
            raise InternalServerError(str(e)) from e

    def __validate_user(self, token: str) -> Session:
        try:
            user, session = self.__validate.user_session_token(token)
            return session
        except NotFoundError as e:
            raise NotFoundError(str(e)) from e

    def __send_message(self, session: Session):
        try:
            params = json.dumps({
                "session_id": session.session_id
            })
            log_session(session=params, action="chat_leave")
            self.__forward_message.send_message(params=params, action="/chat/leave")
        except BadRequestError as e:
            log_error(error=e, message=session.to_dict())
            raise BadRequestError(str(e)) from e
