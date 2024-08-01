from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.chat.chat_leave import  ChatLeave as ChatLeaveInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.main.logs.logs import log_session


class ChatLeaveController(ControllerInterface):

    def __init__(self, use_case: ChatLeaveInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get('token')
        log_session(session=[token], action="chat_leave_controller")
        response = self.__use_case.leave(token=token)

        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
