from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.group import Group


class ChatJoin(ABC):

    @abstractmethod
    def join(self, group: Group, email: str): pass
