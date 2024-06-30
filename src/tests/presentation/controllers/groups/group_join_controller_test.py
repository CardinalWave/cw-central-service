from src.presentation.controllers.groups.group_join_controller import GroupJoinController
from src.presentation.http_types.http_response import HttpResponse
from src.tests.data.mocks.groups.group_join import GroupJoinSpy

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
                    "token": "bola2014",
                    "email": "vmarques@outlook.com",
                    "username": "Lua",
                    "group_title": "GLOBAL",
                    "group_id": "cddf58c6-4dbf-4744-a5a9-549bba02c65b",
                    "title": "GLOBAL"
                    }


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = GroupJoinSpy()
    group_join_controller = GroupJoinController(use_case)

    response = group_join_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is not None
