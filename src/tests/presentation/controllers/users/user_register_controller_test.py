from src.presentation.controllers.users.user_register_controller import UserRegisterController
from src.tests.data.mocks.users.user_register import UserRegisterSpy
from src.presentation.http_types.http_response import HttpResponse
from src.tests.main.mock.logs import LogSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = { "email": "lua@outlook.com", "username": "Lua", "password": "oitooito"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    logger = LogSpy()
    user_register_controller = UserRegisterController(use_case, logger)

    response = user_register_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is not None
