from src.presentation.controllers.user_login_controller import UserLoginController
from src.data.tests.user_login import UserLoginSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = { "email": "lua@outlook.com", "password": "lu@Pelud@" }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserLoginSpy()
    user_finder_controller = UserLoginController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
