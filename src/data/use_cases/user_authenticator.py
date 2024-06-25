import http.client
import json
from src.domain.use_cases.user_authenticator import UserAuthenticator as UserAuthenticatorInterface
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register
from src.data.erros.domain_errors import BadRequestError, InternalServerError, NotFoundError


class UserAuthenticator(UserAuthenticatorInterface):
    cw_auth_service = ""

    @classmethod
    def login(cls, login: Login) -> User:
        try: 
            url = cls.cw_auth_service
            request = cls.__request_auth(params=login, url=url, action="login")
            return request
        except Exception as e:
            raise BadRequestError(e)

    @classmethod
    def register(cls, register: Register) -> User:
        try: 
            url = cls.cw_auth_service
            request = cls.__request_auth(params=register.to_json(), url=url, action="regiter")
            return request
        except Exception as e:
            raise BadRequestError(e)


    @classmethod
    def logout(cls, user: User) -> User:
        try:
            url = cls.cw_auth_service
            request = cls.__request_auth(params=user.to_json(), url=url, action="logout")
            return request
        except Exception as e:
            raise BadRequestError(e)

    @staticmethod
    def __request_auth(params: any, url, action) -> User:
        try:
            headers = {
                'Content-type': 'application/json'
            }

            conn = http.client.HTTPConnection(url)
            route = "/user/"+action
            conn.request("POST", route, params, headers, timeout=60)
            response = conn.getresponse()
            if response.status != 200:
                raise ValueError("Request error")

            data = response.read()
            json_data = json.loads(data)
            conn.close()

            return User(token=json_data['token'][0],
                        username=json_data['username'],
                        email=json_data['email'])
        except Exception as e:
            raise InternalServerError(str(e))
