from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.entities.groups import Groups as GroupsEntity
from src.infra.db.entities.users_groups import UsersGroups as UsersGroupsEntity

class UsersGroupsRepositoryInterface(ABC):

    @abstractmethod
    def join_user(self, id: str, secure_email: str, group_title: str, group_id: str, updated_at: datetime) -> UsersGroupsEntity:pass

    @abstractmethod
    def select_user_relations(self, secure_email: str) ->  List[UsersGroupsEntity]: pass

    @abstractmethod
    def select_group_relations(self, group_id: str) ->  List[UsersGroupsEntity]: pass

    @abstractmethod
    def update_relation(self, secure_email: str, group_id: str, updated_at: datetime) ->  UsersGroupsEntity: pass
