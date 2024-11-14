from src.presentation.controllers.users.user_login_controller import UserLoginController
from src.tests.data.mocks.users.user_login import UserLoginSpy
from src.presentation.http_types.http_response import HttpResponse
from src.tests.main.mock.logs import LogSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
                "session_id": "session_idkmadmadada",
                "device": "esp8266_01",
                "email": "test@outlook.com",
                "password": "senhadasd"
        }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserLoginSpy()
    logger_spy = LogSpy()
    user_login_controller = UserLoginController(use_case, logger_spy)

    response = user_login_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is not None
