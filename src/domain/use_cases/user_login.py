from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.login import Login

class UserLogin(ABC):

    @abstractmethod
    def login(self, login: Login) -> Dict: pass
