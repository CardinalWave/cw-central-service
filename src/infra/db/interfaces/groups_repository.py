from abc import ABC, abstractmethod
from src.infra.db.entities.groups import Groups as GroupsEntity

class GroupsRepositoryInterface(ABC):

    @abstractmethod
    def add_group(self, id: str, title: str) -> GroupsEntity:pass

    @abstractmethod
    def select_title(self, title: str) -> GroupsEntity:pass
