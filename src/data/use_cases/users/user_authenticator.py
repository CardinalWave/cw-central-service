#pylint: disable=unused-variable, line-too-long, unused-argument
import json
import random
import string
import uuid
import http.client
from src.domain.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register
from src.data.erros.domain_errors import BadRequestError, InternalServerError
from src.main.logs.logs import Log


class UserAuthenticator(UserAuthInterface):
    def __init__(self):
        self.__auth_service_ip = "cw-auth-service"
        self.__auth_service_port = 5055
        self.__logger = Log()

    def login(self, login: Login) -> User:
        try:
            params = login.to_json()
            return self.__request_auth(params=params, action="login")
            # return User(username="Teste",
            #             email="teste@email.com",
            #             token="token")
        except Exception as e:
            raise BadRequestError(f"Login failed: {e}") from e

    def register(self, register: Register) -> User:
        try:
            params = register.to_json()
            return self.__request_auth(params=params, action="register")
        except Exception as e:
            raise BadRequestError(f"Registration failed: {str(e)}") from e

    def logout(self, user: User) -> User:
        try:
            params = {"token": user.token}
            return self.__request_auth(params=params, action="logout")
            # return User(username="Teste",
            #             email="teste@email.com",
            #             token="token")
        except Exception as e:
            raise BadRequestError(f"Logout failed: {str(e)}") from e

    def __request_auth(self, params: dict, action: str) -> User:
        try:
            self.__logger.log_session(session=params, action=f'request cw-auth-service '
                                                             f'{self.__auth_service_ip}:'
                                                             f'{self.__auth_service_port} - {action}')
            headers = {'Content-Type': 'application/json'}
            conn = http.client.HTTPConnection(host=self.__auth_service_ip, port=self.__auth_service_port)
            conn.request("POST", action, params, headers)
            conn.sock.settimeout(10)
            response = conn.getresponse()
            if response.status != 200:
                raise ValueError("Request error")
            data = response.read()
            json_data = json.loads(data)
            self.__logger.log_session(session=params, action=f'return {json_data}')
            conn.close()
            return User(
                token=json_data.get("token"),
                username=json_data.get("username"),
                email=json_data.get("email")
            )
        except Exception as e:
            raise InternalServerError(f"Error in {action}: {str(e)}") from e