from src.domain.models.user import User
from src.domain.use_cases.user_logout import UserLogout as UserLogoutInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_authenticator import UserAuthenticator as UserAuthenticatorInterface

class UserLogout(UserLogoutInterface):
    def __init__(self, users_repository: UsersRepositoryInterface,
                user_authenticator: UserAuthenticatorInterface) -> None:
        self.__users_repository = users_repository
        self.__user_authenticator = user_authenticator

    @classmethod
    def logout(cls, user: User) -> None:
        cls.__authentication(user=user)
        cls.__logout_repo(user)

    def __authentication(self, user: User) -> None:
        self.__user_authenticator.logout(user)

    def __logout_repo(self, user: User) -> None:
        self.__users_repository.remove_user(user.token)
