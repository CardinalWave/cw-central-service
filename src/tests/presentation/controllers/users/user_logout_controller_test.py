from src.presentation.controllers.users.user_logout_controller import UserLogoutController
from src.tests.data.mocks.users.user_logout import UserLogoutSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = { "token": "39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                            "email": "lua@outlook.com",
                            "username": "Lua" }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserLogoutSpy()
    user_logout_controller = UserLogoutController(use_case)

    response = user_logout_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is None
