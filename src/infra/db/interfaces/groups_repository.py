from abc import ABC, abstractmethod
from src.infra.db.entities.users import Users as UsersEntity

class GroupsRepositoryInterface(ABC):

    @abstractmethod
    def add_group(self, id: str, title: str) -> None:pass

    @abstractmethod
    def select_title(self, title: str) -> None:pass
