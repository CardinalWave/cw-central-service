from src.presentation.controllers.groups.group_join_controller import GroupJoinController
from src.presentation.http_types.http_response import HttpResponse
from src.tests.data.mocks.groups.group_join import GroupJoinSpy

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
                    "token": "7a7d1fab-f717-46de-8743-50cadfef383b",
                    "group_id": "3421584c-3248-487e-b351-b24b162b2f39"
                    }


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = GroupJoinSpy()
    group_join_controller = GroupJoinController(use_case)

    response = group_join_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is not None
