from src.presentation.controllers.groups.group_list_controller import GroupListController
from src.presentation.http_types.http_response import HttpResponse
from src.tests.data.mocks.groups.group_list import GroupListSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {"token": "bola2014",
                     "email": "vmarques@outlook.com",
                     "username": "Lua"}


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = GroupListSpy()
    group_list_controller = GroupListController(use_case)

    response = group_list_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is not None
