from abc import ABC, abstractmethod
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register

class UserAuthenticator(ABC):

    @abstractmethod
    def login(self, login: Login) -> User: pass

    @abstractmethod
    def register(self, register: Register) -> User: pass

    @abstractmethod
    def logout(self, user: User) -> None: pass
