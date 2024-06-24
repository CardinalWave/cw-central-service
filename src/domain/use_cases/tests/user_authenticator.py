from typing import List
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register
from src.domain.use_cases.user_authenticator import UserAuthenticatorInterface


class UserAuthenticatorSpy(UserAuthenticatorInterface):

    @classmethod
    def login(cls, login: Login) -> User:
        instance = cls
        return cls._request_auth(instance, login, login.email)

    @classmethod
    def register(cls, register: Register):
        instance = cls
        return cls._request_auth(instance, register, register.email)

    def _request_auth(self, request: any, email: str) -> None:
        return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee", username="Lua", email=email)