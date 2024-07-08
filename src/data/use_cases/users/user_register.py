#pylint: disable=broad-exception-raised
from typing import Dict
from src.domain.use_cases.users.user_resgister import UserRegister as UserRegisterInterface
from src.data.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface
from src.domain.models.register import Register
from src.domain.models.user import User
from src.data.erros.domain_errors import BadRequestError, InternalServerError


class UserRegister(UserRegisterInterface):

    def __init__(self, user_authenticator: UserAuthInterface) -> None:
        self.__user_authenticator = user_authenticator

    def register(self, register: Register) -> Dict:
        try:
            self.__validate_username(register.username)
            self.__validate_email(register.email)
            self.__validate_password(register.password)
            auth = self.__authentication(register=register)
            response = self.__format_response(user=auth)
            return response
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    @staticmethod
    def __validate_username(username: str) -> None:
        if not username.isalpha():
            raise BadRequestError('Nome invalido para o registro')

        if len(username) > 20:
            raise BadRequestError('Nome muito grande para o registro')

    @staticmethod
    def __validate_email(email: str) -> None:
        if not "@" in email:
            raise BadRequestError('Email ou senha invalido')

    @staticmethod
    def __validate_password(password: str) -> None:
        if 8 > len(password) > 250:
            raise BadRequestError('Senha invalida')

    def __authentication(self, register: Register) -> User:
        return self.__user_authenticator.register(register)

    @staticmethod
    def __format_response(user: User) -> Dict:
        return user.to_dict()
