#pylint: disable=unused-argument

import uuid
from src.domain.models.group import Group
from src.domain.use_cases.groups.group_list import GroupList as GroupListInterface


class GroupListSpy(GroupListInterface):

    def list(self, token: str) -> list[Group]:
        group_list = [
            Group(group_id=str(uuid.uuid4()), title="Grupo1").to_dict(),
            Group(group_id=str(uuid.uuid4()), title="Grupo2").to_dict(),
            Group(group_id=str(uuid.uuid4()), title="Grupo3").to_dict()]
        return group_list
