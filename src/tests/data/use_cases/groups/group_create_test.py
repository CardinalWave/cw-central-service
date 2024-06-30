import pytest
from typing import List
from src.domain.models.user import User
from src.domain.models.group import Group
from src.infra.db.entities.groups import Groups as GroupEntity
from src.data.use_cases.groups.group_create import GroupCreate
from src.tests.data.mocks.relations.user_group import UserGroupSpy
from src.tests.infra.mocks.groups_repository import GroupsRepositorySpy

@pytest.fixture
def mock_group():
    return Group(group_id="dasd-dasd-dads", title="testGroupMock")

def test_create(mock_group):
    repository = GroupsRepositorySpy()
    group_create = GroupCreate(group_repository=repository)
    response = group_create.create(mock_group)

    assert response is not None
    assert response is not type(Group)
    assert response is not type(GroupEntity)
