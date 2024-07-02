from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.users.user_login import UserLogin as UserLoginInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.models.login import Login


class UserLoginController(ControllerInterface):

    def __init__(self, use_case: UserLoginInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        email = http_request.body.get("email")
        password = http_request.body.get('password')
        login = Login(email=email, password=password)
        response = self.__use_case.login(login)

        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
