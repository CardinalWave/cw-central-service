import uuid
import datetime as dt
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.users_groups import UsersGroups
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface

class UserGroupSpy(UserGroupInterface):

    def join_user(self, user: User, group: Group) -> Dict:
        return UsersGroups(id=str(uuid.uuid4()),
                           secure_email=user.email,
                           group_title=group.title,
                           group_id=group.group_id,
                           updated_at=str(dt.datetime.now)).to_dict()

    def select_user_relations(self, secure_email: str) -> list[Group]:
        group_list = [
                    Group(group_id=str(uuid.uuid4()), title="Grupo1"),
                    Group(group_id=str(uuid.uuid4()), title="Grupo2"),
                    Group(group_id=str(uuid.uuid4()), title="Grupo3")]
        return group_list

    def select_group_relations(self, group_id: str) -> list[User]:
        pass

    def update_relation(self, user: User, group: Group) -> Dict:
        pass
