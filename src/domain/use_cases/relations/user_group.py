from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models.user import User
from src.domain.models.group import Group

class UserGroup(ABC):

    @abstractmethod
    def join_user(self, user: User, group: Group) -> Dict: pass

    @abstractmethod
    def select_user_relations(self, secure_email: str) ->  List[Group]: pass

    @abstractmethod
    def select_group_relations(self, group_id: str) ->  List[User]: pass

    @abstractmethod
    def update_relation(self, user: User, group: Group) -> Dict: pass
