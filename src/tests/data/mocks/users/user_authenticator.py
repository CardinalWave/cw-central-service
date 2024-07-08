from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register
from src.domain.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface


class UserAuthenticatorSpy(UserAuthInterface):

    @classmethod
    def login(cls, login: Login) -> User:
        return cls.__request_auth(email=login.email)

    @classmethod
    def register(cls, register: Register) -> User:
        return cls.__request_auth(email=register.email)

    @classmethod
    def logout(cls, user: User) -> None: pass

    @staticmethod
    def __request_auth(email: str) -> User:
        return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee", username="Lua", email=email)
