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
        email = http_request.body.get("email")
        username = http_request.body.get("username")
        user = User(token=token, email=email, username=username)
        group_title = http_request.body.get("group_title")
        group_id = http_request.body.get("group_id")
        group = Group(group_id=group_id, title=group_title)

        response = self.__use_case.join(user, group)

        return HttpResponse(
            status_code=200,
            body={ "payload":response }
        )
