import uuid
import datetime as dt
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.users_groups import UsersGroups
from src.domain.use_cases.groups.group_join import GroupJoin as GroupJoinInterface

class GroupJoinSpy(GroupJoinInterface):

    def join(self, user: User, group: Group) -> UsersGroups:
        return UsersGroups(id=uuid.uuid4(), secure_email="a6b00b3b232a4f30ef8ceee8a8a40ad677fcd762c9fc0d7b2aab20f51b1f9179", 
                           group_title=group.title, 
                           group_id=group.group_id, 
                           updated_at=dt.datetime.now())
    
    def join_global(self, user: User) -> UsersGroups:
         return UsersGroups(id=uuid.uuid4(), secure_email="a6b00b3b232a4f30ef8ceee8a8a40ad677fcd762c9fc0d7b2aab20f51b1f9179", 
                           group_title="GLOBAL", 
                           group_id="GLOBAL_ID", 
                           updated_at=dt.datetime.now())
