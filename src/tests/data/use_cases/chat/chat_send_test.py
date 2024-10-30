from src.data.use_cases.chat.chat_send import ChatSend
from src.tests.data.mocks.relations.validate import ValidateSpy
from src.tests.data.mocks.chat.forward_message import ForwardMessageSpy
from src.tests.main.mock.logs import LogSpy
from src.tests.data.mocks.relations.user_group import UserGroupSpy


def test_send():
    validate = ValidateSpy()
    forward_message = ForwardMessageSpy()
    user_group = UserGroupSpy()
    logger = LogSpy()

    chat_send = ChatSend(validate=validate,
                         forward_message=forward_message,
                         logger=logger,
                         user_group=user_group)

    mocked_token = "de5e8591-180b-4158-a321-3686588638db"
    mocked_group_id = "e52de285-44ad-4d55-8220-aec9d370fe95"
    chat_send.send(group_id=mocked_group_id, token=mocked_token, message="Ola 123 $%")


def test_error_validate_user():
    validate = ValidateSpy()
    forward_message = ForwardMessageSpy()
    user_group = UserGroupSpy()
    logger = LogSpy()

    chat_send = ChatSend(validate=validate,
                         forward_message=forward_message,
                         logger=logger,
                         user_group=user_group)

    mocked_token = "token_error"
    mocked_group_id = "e52de285-44ad-4d55-8220"
    try:
        chat_send.send(group_id=mocked_group_id, token=mocked_token, message="Test")
        assert False
    except Exception as exception:
        assert str(exception) == "assert False"


def test_error__validate_group():
    validate = ValidateSpy()
    forward_message = ForwardMessageSpy()
    user_group = UserGroupSpy()
    logger = LogSpy()

    chat_send = ChatSend(validate=validate,
                         forward_message=forward_message,
                         logger=logger,
                         user_group=user_group)

    mocked_token = "de5e8591-180b-4158-a321-3686588638db"
    mocked_group_id = ""
    try:
        chat_send.send(group_id=mocked_group_id, token=mocked_token, message="chat_send@@423")
        assert False
    except Exception as exception:
        assert str(exception) == "assert False"
