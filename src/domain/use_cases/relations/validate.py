from abc import ABC
from src.domain.models.user import User
from src.domain.models.group import Group


class Validate(ABC):

    def user_token(self, token: str) -> User: pass

    def user_email(self, email: str) -> User: pass

    def user_session_token(self, token) -> tuple: pass

    def group_id(self, group_id: str,  email: str) -> Group: pass

    def group_title(self, group_title: str,  email: str) -> Group: pass
