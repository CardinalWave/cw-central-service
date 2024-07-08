from src.data.use_cases.chat.chat_join import ChatJoin
from src.tests.data.mocks.chat.forward_message import ForwardMessageSpy
from src.tests.data.mocks.relations.validate import ValidateSpy


def test_join():
    forward_message = ForwardMessageSpy()
    validate = ValidateSpy()
    chat_join = ChatJoin(forward_message=forward_message,
                         validate=validate)

    mocked_token = "de5e8591-180b-4158-a321-3686588638db"
    mocked_group_id = "e52de285-44ad-4d55-8220-aec9d370fe95"

    response = chat_join.join(group_id=mocked_group_id, token=mocked_token)

    assert response.get("group_id") == mocked_group_id
