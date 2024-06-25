from src.domain.use_cases.user_logout import UserLogout as UserLogoutInterface
from src.domain.models.user import User

class UserLogoutSpy(UserLogoutInterface):

    @classmethod
    def logout(cls, user: User) -> None: pass
