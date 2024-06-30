import uuid
from typing import List
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.use_cases.groups.group_list import GroupList as GroupListInterface

class GroupListSpy(GroupListInterface):

    def list(self, user: User) -> List[Group]:
        group_list = [
                    Group(group_id=uuid.uuid4(), title="Grupo1").to_dict(),
                    Group(group_id=uuid.uuid4(), title="Grupo2").to_dict(),
                    Group(group_id=uuid.uuid4(), title="Grupo3").to_dict()]
        return group_list