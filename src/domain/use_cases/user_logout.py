from abc import ABC, abstractmethod
from src.domain.models.user import User

class UserLogout(ABC):

    @abstractmethod
    def logout(self, user: User) -> None: pass
