from abc import ABC, abstractmethod
from src.infra.db.entities.groups import Groups as GroupsEntity

class GroupsRepositoryInterface(ABC):

    @abstractmethod
    def add_group(cls, id: str, title: str) -> GroupsEntity:pass

    @abstractmethod
    def select_title(cls, title: str) -> GroupsEntity:pass
