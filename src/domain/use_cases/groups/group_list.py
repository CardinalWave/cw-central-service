from abc import ABC, abstractmethod
from typing import List
from src.domain.models.user import User
from src.domain.models.group import Group

class GroupList(ABC):

    @abstractmethod
    def list(self, user: User) -> List[Group] : pass
