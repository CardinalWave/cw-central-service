from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.chat.chat_send import ChatSend as ChatSendInterface
from src.main.logs.logs_interface import LogInterface

class ChatSendController(ControllerInterface):

    def __init__(self, use_case: ChatSendInterface, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get("token")
        group_id = http_request.body.get("group_id")
        message = http_request.body.get("message")
        response = self.__use_case.send(token=token, group_id=group_id, message=message)
        self.__logger.log_session(session=[token, group_id, message], action="controller_send")
        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
