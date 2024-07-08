from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.chat.chat_send import ChatSend as ChatSendInterface


class ChatSendController(ControllerInterface):

    def __init__(self, use_case: ChatSendInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get("token")
        group_id = http_request.body.get("group_id")
        message = http_request.body.get("message")
        response = self.__use_case.send(token=token, group_id=group_id, message=message)

        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
