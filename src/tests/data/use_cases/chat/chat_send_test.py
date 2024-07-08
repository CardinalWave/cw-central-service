from src.data.use_cases.chat.chat_send import ChatSend
from src.tests.data.mocks.relations.validate import ValidateSpy
from src.tests.data.mocks.chat.forward_message import ForwardMessageSpy


def test_send():
    validate = ValidateSpy()
    forward_message = ForwardMessageSpy()

    chat_send = ChatSend(validate=validate,
                         forward_message=forward_message)

    mocked_token = "de5e8591-180b-4158-a321-3686588638db"
    mocked_group_id = "e52de285-44ad-4d55-8220-aec9d370fe95"

    response = chat_send.send(group_id=mocked_group_id, token=mocked_token, message="Ola 123 $%")

    assert response.get("group_id") == mocked_group_id
