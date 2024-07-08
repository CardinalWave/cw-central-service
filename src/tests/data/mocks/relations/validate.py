from uuid import uuid4
from src.domain.models.group import Group
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.domain.models.user import User
from src.domain.models.session import Session


class ValidateSpy(ValidateInterface):

    @classmethod
    def user_email(cls, email: str) -> User:
        return User(token=str(uuid4()), email=email, username="TestName")

    @classmethod
    def user_token(cls, token: str) -> User:
        return User(token=str(uuid4()), email="test@email.com", username="TestName")

    @classmethod
    def user_session_token(cls, token) -> tuple:
        user = User(token=token, email="test@email.com", username="TestName")
        session = Session(session_id=str(uuid4()), device="esp8266_01")
        return user, session

    @classmethod
    def group_id(cls, group_id: str,  email: str) -> Group:
        return Group(group_id=group_id, title="TestGroup")

    @classmethod
    def group_title(cls, group_title: str,  email: str) -> Group:
        return Group(group_id=str(uuid4()), title=group_title)
