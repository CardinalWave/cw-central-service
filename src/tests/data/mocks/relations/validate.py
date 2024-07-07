from uuid import uuid4

from src.domain.models.group import Group
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.domain.models.user import User


class ValidateSpy(ValidateInterface):

    @classmethod
    def user_email(self, email: str) -> User:
        return User(token=str(uuid4()), email=email, username="TestName")

    @classmethod
    def user_token(self, token: str) -> User:
        return User(token=str(uuid4()), email="test@email.com", username="TestName")

    @classmethod
    def group_id(self, group_id: str) -> Group:
        return Group(group_id=group_id, title="TestGroup")

    @classmethod
    def group_title(self, group_title: str) -> Group:
        return Group(group_id=str(uuid4()), title=group_title)
