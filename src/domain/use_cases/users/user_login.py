from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.login import Login
from src.domain.models.session import Session


class UserLogin(ABC):

    @abstractmethod
    def login(self, login: Login, session: Session) -> Dict: pass
