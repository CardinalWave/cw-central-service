from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.users.user_resgister import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.models.register import Register
from src.main.logs.logs_interface import LogInterface


class UserRegisterController(ControllerInterface):

    def __init__(self, use_case: UserRegisterInterface, logger: LogInterface) -> None:
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        email = http_request.body.get("email")
        username = http_request.body.get('username')
        password = http_request.body.get('password')
        register = Register(email=email, username=username, password=password)
        self.__logger.log_session(session=[email, username, "********"], action="user_register_controller")
        response = self.__use_case.register(register)

        return HttpResponse(
            status_code=200,
            body={"payload": response}
        )
