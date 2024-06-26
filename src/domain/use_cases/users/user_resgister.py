from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.register import Register

class UserRegister(ABC):

    @abstractmethod
    def register(self,register: Register) -> Dict: pass
