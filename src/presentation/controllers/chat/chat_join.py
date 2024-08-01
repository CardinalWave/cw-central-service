from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.chat.chat_join import ChatJoin as ChatJoinInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.main.logs.logs import log_session


class ChatJoinController(ControllerInterface):

    def __init__(self, use_case: ChatJoinInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get('token')
        group_id = http_request.body.get('group_id')
        log_session(session=[token, group_id], action="chat_join_controller")
        response = self.__use_case.join(group_id=group_id, token=token)

        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
