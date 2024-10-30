from src.data.use_cases.chat.chat_join import ChatJoin
from src.tests.data.mocks.chat.forward_message import ForwardMessageSpy
from src.tests.data.mocks.relations.validate import ValidateSpy
from src.tests.data.mocks.relations.user_group import UserGroupSpy
from src.tests.main.mock.logs import LogSpy


def test_join():
    logger = LogSpy()
    forward_message = ForwardMessageSpy()
    validate = ValidateSpy()
    user_group = UserGroupSpy()
    chat_join = ChatJoin(forward_message=forward_message,
                         validate=validate,
                         user_group=user_group,
                         logger=logger)

    mocked_token = "de5e8591-180b-4158-a321-3686588638db"
    mocked_group_id = "e52de285-44ad-4d55-8220-aec9d370fe95"

    chat_join.join(group_id=mocked_group_id, token=mocked_token)


def test_error_validate_user():
    logger = LogSpy()
    forward_message = ForwardMessageSpy()
    validate = ValidateSpy()
    user_group = UserGroupSpy()
    chat_join = ChatJoin(forward_message=forward_message,
                         validate=validate,
                         user_group=user_group,
                         logger=logger)

    mocked_token = "token_error"
    mocked_group_id = "e52de285-44ad-4d55-8220"
    try:
        chat_join.join(group_id=mocked_group_id, token=mocked_token)
        assert False
    except Exception as exception:
        assert str(exception) == "'NoneType' object has no attribute 'group_id'"


def test_error__validate_group():
    logger = LogSpy()
    forward_message = ForwardMessageSpy()
    validate = ValidateSpy()
    user_group = UserGroupSpy()
    chat_join = ChatJoin(forward_message=forward_message,
                         validate=validate,
                         user_group=user_group,
                         logger=logger)

    mocked_token = "de5e8591-180b-4158-a321-3686588638db"
    mocked_group_id = ""
    try:
        chat_join.join(group_id=mocked_group_id, token=mocked_token)
        assert False
    except Exception as exception:
        assert str(exception) == "'NoneType' object has no attribute 'group_id'"
