from abc import ABC, abstractmethod
from src.domain.models.user import User
from src.domain.models.group import Group
from src.domain.models.users_groups import UsersGroups


class GroupJoin(ABC):

    @abstractmethod
    def join(self, token: str, group: str) -> UsersGroups: pass

