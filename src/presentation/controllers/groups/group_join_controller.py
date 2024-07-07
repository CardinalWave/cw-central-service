from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.groups.group_join import GroupJoin as GroupJoinInterface
from src.domain.models.user import User
from src.domain.models.group import Group


class GroupJoinController(ControllerInterface):

    def __init__(self, use_case: GroupJoinInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get("token")
        group_id = http_request.body.get("group_id")

        response = self.__use_case.join(token, group_id)

        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
