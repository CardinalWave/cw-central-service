from src.domain.models.user import User
from src.domain.use_cases.users.user_logout import UserLogout as UserLogoutInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface
from src.data.erros.domain_errors import BadRequestError

class UserLogout(UserLogoutInterface):
    def __init__(self, users_repository: UsersRepositoryInterface,
                user_authenticator: UserAuthInterface) -> None:

        self.__users_repository = users_repository
        self.__user_authenticator = user_authenticator

    def logout(self, user: User) -> None:
        try:
            self.__authentication(user=user)
            self.__logout_repo(user)
            return "success"
        except BadRequestError:
            return "failed"
        except Exception:
            return "failed"

    def __authentication(self, user: User) -> None:
        self.__user_authenticator.logout(user)

    def __logout_repo(self, user: User) -> None:
        self.__users_repository.remove_user(user.token)
