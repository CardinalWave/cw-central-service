from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_resgister import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.models.register import Register

class UserRegisterController(ControllerInterface):

    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        email = http_request.query_params["email"]
        username = http_request.query_params["username"]
        password = http_request.query_params["password"]
        register = Register(email=email, username=username, password=password)
        response = self.__use_case.register(register)

        return HttpResponse(
            status_code=200,
            body={ "data":response }
        )
