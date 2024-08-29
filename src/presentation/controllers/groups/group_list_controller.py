from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.groups.group_list import GroupList as GroupListInterface
from src.domain.models.user import User


class GroupListController(ControllerInterface):

    def __init__(self, use_case: GroupListInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get("token")
        response = self.__use_case.list(token)

        return HttpResponse(
            status_code=200,
            body={ "payload":response }
        )
