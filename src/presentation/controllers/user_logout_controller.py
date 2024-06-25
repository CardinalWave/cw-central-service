from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.models.user import User
from src.domain.use_cases.user_logout import UserLogout as UserLogoutInterface

class UserLogoutController(ControllerInterface):

    def __init__(self, use_case: UserLogoutInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.body.get('token')
        email = http_request.body.get("email")
        username = http_request.body.get('username')
        user = User(token=token, email=email, username=username)
        response = self.__use_case.logout(user)

        return HttpResponse(
            status_code=200,
            body={ "payload":response }
        )
