import pytest
from typing import List
from src.domain.models.user import User
from src.domain.models.group import Group
from src.infra.db.entities.groups import Groups as GroupEntity
from src.data.use_cases.groups.group_join import GroupJoin
from src.tests.data.mocks.relations.user_group import UserGroupSpy
from src.tests.infra.mocks.groups_repository import GroupsRepositorySpy

@pytest.fixture
def mock_user():
    return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
            username='Lua', email='lua@outlook.com')

@pytest.fixture
def mock_group():
    return Group(group_id="sda-dasd-dasda", title="TestGroup")

def test_join(mock_user, mock_group):
    groups_repository = GroupsRepositorySpy()
    users_groups = UserGroupSpy()
    group_join = GroupJoin(group_repository=groups_repository, users_groups=users_groups)
    response = group_join.join(mock_user, mock_group)

    assert response is not None
    assert response is not type(Group)
    assert response is not type(GroupEntity)
