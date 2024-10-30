from src.domain.models.user import User
from src.domain.use_cases.users.user_logout import UserLogout as UserLogoutInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface
from src.data.erros.domain_errors import BadRequestError
from src.main.logs.logs_interface import LogInterface


class UserLogout(UserLogoutInterface):
    def __init__(self, users_repository: UsersRepositoryInterface,
                 user_authenticator: UserAuthInterface, logger: LogInterface) -> None:

        self.__users_repository = users_repository
        self.__user_authenticator = user_authenticator
        self.__logger = logger

    def logout(self, user: User) -> str:
        try:
            self.__authentication(user=user)
            status = self.__logout_repo(user)
            self.__logger.log_session(session=user.token, action="user_logout")
            return status
        except BadRequestError:
            return "failed"

    def __authentication(self, user: User) -> None:
        self.__user_authenticator.logout(user)

    def __logout_repo(self, user: User) -> str:
        return self.__users_repository.remove_user(user.token)
