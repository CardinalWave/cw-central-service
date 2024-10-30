#pylint: disable=redefined-outer-name
import pytest
from src.domain.models.user import User
from src.domain.models.group import Group
from src.infra.db.entities.groups import Groups as GroupEntity
from src.data.use_cases.groups.group_list import GroupList
from src.tests.data.mocks.relations.user_group import UserGroupSpy

@pytest.fixture
def mock_user():
    return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
            username='Lua', email='lua@outlook.com')

def test_list(mock_user):
    users_groups = UserGroupSpy()
    group_list = GroupList(users_groups)

    response = group_list.list(mock_user)

    assert response is not None
    assert response[0] is not type(Group)
    assert response[0] is not type(GroupEntity)
