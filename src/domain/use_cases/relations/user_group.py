from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.user import User
from src.domain.models.group import Group


class UserGroup(ABC):

    @abstractmethod
    def join_user(self, user: User, group: Group) -> Dict: pass

    @abstractmethod
    def select_user_relations(self, email: str) -> list[Group]: pass

    @abstractmethod
    def select_group_relations(self, group_id: str) -> list[User]: pass

    @abstractmethod
    def update_relation(self, user: User, group: Group) -> Dict: pass
