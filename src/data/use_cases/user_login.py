#pylint: disable=broad-exception-raised
from typing import Dict
from src.domain.use_cases.user_login import UserLogin as UserLoginInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_authenticator import UserAuthenticator as UserAuthenticatorInterface
from src.domain.models.user import User
from src.domain.models.login import Login

class UserLogin(UserLoginInterface):
    def __init__(self, users_repository: UsersRepositoryInterface,
                user_authenticator: UserAuthenticatorInterface) -> None:

        self.__users_repository = users_repository
        self.__user_authenticator = user_authenticator

    def login(self, login: Login) -> Dict:
        self.__validate_email(login.email)
        self.__validate_password(login.password)
        self.__search_user(login=login)
        auth = self.__authentication(login=login)
        self.__save_login(user=auth)
        response = self.__format_response(user=auth)
        return response

    @staticmethod
    def __validate_email(email: str) -> None:
        if "@" not in email:
            raise Exception('Email ou senha invalido')

    @staticmethod
    def __validate_password(password: str) -> None:
        if len(password) < 8:
            raise Exception('Email ou senha invalido')

    def __search_user(self, login: Login) -> None:
        users = self.__users_repository.select_email(email=login.email)
        if users:
            raise Exception('Usuario logado')

    def __authentication(self, login: Login) -> User:
        return self.__user_authenticator.login(login)

    def __save_login(self, user: User) -> None:
        self.__users_repository.insert_user(token=user.token,
                                            email=user.email,
                                            username=user.username)

    @staticmethod
    def __format_response(user: User) -> Dict:
        return user.to_dict()
