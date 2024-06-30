from src.presentation.controllers.groups.group_create_controller import GroupCreateController
from src.presentation.http_types.http_response import HttpResponse
from src.tests.data.mocks.groups.group_create import GroupCreateSpy

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = { "title": "groupTest" }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = GroupCreateSpy()
    group_create_controller = GroupCreateController(use_case)

    response = group_create_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is not None
