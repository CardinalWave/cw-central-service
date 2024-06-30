import uuid
import datetime as dt
from typing import Dict, List
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.users_groups import UsersGroups
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface

class UserGroupSpy(UserGroupInterface):

    def join_user(self, user: User, group: Group) -> Dict:
        return UsersGroups(id=uuid.uuid4(),
                           secure_email=user.email,
                           group_title=group.title,
                           group_id=group.group_id,
                           updated_at=dt.datetime.now).to_dict()
    
    def select_user_relations(self, secure_email: str) -> List[Group]:
        group_list = [
                    Group(group_id=uuid.uuid4(), title="Grupo1"),
                    Group(group_id=uuid.uuid4(), title="Grupo2"),
                    Group(group_id=uuid.uuid4(), title="Grupo3")]
        return group_list
    
    def select_group_relations(self, group_id: str) -> List[User]:
        return super().select_group_relations(group_id)
    
    def update_relation(self, user: User, Group: Group) -> Dict:
        return super().update_relation(user, Group)