from abc import ABC, abstractmethod
from src.domain.models.users_groups import UsersGroups


class GroupJoin(ABC):

    @abstractmethod
    def join(self, token: str, group_id: str) -> UsersGroups: pass
