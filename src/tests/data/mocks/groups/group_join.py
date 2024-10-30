#pylint: disable=line-too-long
import uuid
import datetime as dt
from src.domain.models.users_groups import UsersGroups
from src.domain.use_cases.groups.group_join import GroupJoin as GroupJoinInterface


class GroupJoinSpy(GroupJoinInterface):

    def join(self, token: str, group_id: str) -> UsersGroups:
        return UsersGroups(id=str(uuid.uuid4()),
                           secure_email="a6b00b3b232a4f30ef8ceee8a8a40ad677fcd762c9fc0d7b2aab20f51b1f9179",
                           group_title="TestGroup",
                           group_id=group_id,
                           updated_at=str(dt.datetime.now()))
