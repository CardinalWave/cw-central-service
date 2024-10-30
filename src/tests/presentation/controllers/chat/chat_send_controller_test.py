from src.presentation.controllers.chat.chat_send import ChatSendController
from src.presentation.http_types.http_response import HttpResponse
from src.tests.data.mocks.chat.chat_send import ChatSendSpy
from src.tests.main.mock.logs import LogSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {"token": "5259d7df-c0f7-4729-879f-17d1f91c6100",
                     "group_id": "e52de285-44ad-4d55-8220-aec9d370fe95",
                     "message": "Mensagem teste ok 123 $"
                     }


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = ChatSendSpy()
    logger = LogSpy()
    chat_join_controller = ChatSendController(use_case, logger)

    response = chat_join_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["payload"] is not None
