import uuid
from typing import Dict
from src.domain.models.group import Group
from src.domain.use_cases.groups.group_create import GroupCreate as GroupCreateInterface


class GroupCreateSpy(GroupCreateInterface):

    def create(self, group: Group) -> Dict:
        group_id = str(uuid.uuid4())
        return Group(group_id=group_id, title=group.title).to_dict()
