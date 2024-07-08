from src.domain.models.user import User
from src.domain.use_cases.users.user_logout import UserLogout as UserLogoutInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.users.user_authenticator import UserAuthenticator as UserAuthInterface
from src.domain.enums.UserStatusType import UserStatusType
from src.domain.use_cases.relations.user_status import UserStatus as UserStatusInterface
from src.data.erros.domain_errors import BadRequestError


class UserLogout(UserLogoutInterface):
    def __init__(self, users_repository: UsersRepositoryInterface,
                 user_authenticator: UserAuthInterface,
                 user_status: UserStatusInterface) -> None:

        self.__users_repository = users_repository
        self.__user_authenticator = user_authenticator
        self.__user_status = user_status

    def logout(self, user: User) -> str:
        try:
            self.__authentication(user=user)
            status = self.__logout_repo(user)
            self.__user_status.update_status(UserStatusType.ONLINE)
            return status
        except BadRequestError:
            return "failed"
        except Exception:
            return "failed"

    def __authentication(self, user: User) -> None:
        # self.__user_authenticator.logout(user)
        pass

    def __logout_repo(self, user: User) -> str:
        return self.__users_repository.remove_user(user.token)
