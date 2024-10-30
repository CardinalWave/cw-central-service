from abc import ABC, abstractmethod
from typing import List
from src.domain.models.group import Group


class GroupList(ABC):

    @abstractmethod
    def list(self, token: str) -> List[Group]: pass
