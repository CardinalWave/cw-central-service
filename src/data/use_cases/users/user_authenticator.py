import http.client
import json
import random
import string
import uuid

from src.domain.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register
from src.data.erros.domain_errors import BadRequestError, InternalServerError


class UserAuthenticator(UserAuthInterface):
    cw_auth_service = ""

    @classmethod
    def login(cls, login: Login) -> User:
        try:
            url = cls.cw_auth_service
            # request = cls.__request_auth(params=login, url=url, action="login")
            user = User(token=str(uuid.uuid1()),
                        username=''.join(random.choice(string.ascii_letters) for _ in range(6)),
                        email=''.join(random.choice(string.ascii_letters) for _ in range(6)) + '@gmail.com')
            print(user.username)
            print(user.token)
            print(user.email)
            return user
        except Exception as e:
            raise BadRequestError(e) from e

    @classmethod
    def register(cls, register: Register) -> User:
        try:
            url = cls.cw_auth_service
            request = cls.__request_auth(params=register.to_json(), url=url, action="register")
            return request
        except Exception as e:
            raise BadRequestError(e) from e

    @classmethod
    def logout(cls, user: User) -> User:
        try:
            url = cls.cw_auth_service
            request = cls.__request_auth(params=user.to_json(), url=url, action="logout")
            return request
        except Exception as e:
            raise BadRequestError(e) from e

    @staticmethod
    def __request_auth(params: any, url, action) -> User:
        try:
            # headers = {
            #     'Content-type': 'application/json'
            # }
            #
            # conn = http.client.HTTPConnection(url)
            # route = "/user/" + action
            # conn.request("POST", route, params, headers)
            # response = conn.getresponse()
            # if response.status != 200:
            #     raise ValueError("Request error")
            #
            # data = response.read()
            # json_data = json.loads(data)
            # conn.close()
            return User(token=str(uuid.uuid1()),
                        username=''.join(random.choice(string.ascii_letters) for _ in range(6)),
                        email=''.join(random.choice(string.ascii_letters) for _ in range(6)) + '@gmail.com')
        except Exception as e:
            raise InternalServerError(str(e)) from e
