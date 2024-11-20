#pylint: disable=unused-variable, line-too-long, unused-argument
import random
import string
import uuid
import requests
from src.domain.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register
from src.data.erros.domain_errors import BadRequestError, InternalServerError


class UserAuthenticator(UserAuthInterface):
    cw_auth_service = "http://localhost:5010"

    @classmethod
    def login(cls, login: Login) -> User:
        try:
            params = login.to_json()
            return cls.__request_auth(params=params, url=cls.cw_auth_service, action="login")
        except Exception as e:
            raise BadRequestError(f"Login failed: {e}") from e

    @classmethod
    def register(cls, register: Register) -> User:
        try:
            params = register.to_json()
            return cls.__request_auth(params=params, url=cls.cw_auth_service, action="register")
        except Exception as e:
            raise BadRequestError(f"Registration failed: {str(e)}") from e

    @classmethod
    def logout(cls, user: User) -> User:
        try:
            params = {"token": user.token}
            return cls.__request_auth(params=params, url=cls.cw_auth_service, action="logout")
        except Exception as e:
            raise BadRequestError(f"Logout failed: {str(e)}") from e

    @staticmethod
    def __request_auth(params: dict, url: str, action: str) -> User:
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f"{url}/{action}", json=params, headers=headers)

            if response.status_code != 200:
                raise ValueError(f"Error: {response.json().get('error', 'Unknown error')}")

            data = response.json()
            return User(
                token=data.get("token"),
                username=data.get("username"),
                email=data.get("email")
            )
        except Exception as e:
            raise InternalServerError(f"Error in {action}: {str(e)}") from e