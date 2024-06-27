from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.groups.group_create import GroupCreate as GroupCreateInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class GroupCreateController(ControllerInterface):

    def __init__(self, use_case: GroupCreateInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        title = http_request.body.get("title")
        response = self.__use_case.create(title)

        return HttpResponse(
            status_code=200,
            body={ "payload": response }
        )
