from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.chat.chat_join import ChatJoin as ChatJoinInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.main.logs.logs_interface import LogInterface


class ChatJoinController(ControllerInterface):

    def __init__(self, use_case: ChatJoinInterface, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get('token')
        group_id = http_request.body.get('group_id')
        self.__logger.log_session(session=[token, group_id], action="chat_join_controller")
        response = self.__use_case.join(group_id=group_id, token=token)

        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
