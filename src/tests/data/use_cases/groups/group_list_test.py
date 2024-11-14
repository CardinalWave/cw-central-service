#pylint: disable=redefined-outer-name

import pytest
from src.domain.models.group import Group
from src.infra.db.entities.groups import Groups as GroupEntity
from src.data.use_cases.groups.group_list import GroupList
from src.tests.data.mocks.groups.group_join import GroupJoinSpy
from src.tests.data.mocks.relations.user_group import UserGroupSpy
from src.tests.data.mocks.relations.validate import ValidateSpy


@pytest.fixture
def mock_group():
    group_list = []
    group = Group(group_id="0000", title="title")
    return group_list.append(group)

def test_list(mock_group):
    users_groups = UserGroupSpy()
    validate = ValidateSpy()
    group_join = GroupJoinSpy()
    group_list = GroupList(users_groups, validate, group_join)

    response = group_list.list(mock_group)

    assert response is not None
    assert response[0] is not type(Group)
    assert response[0] is not type(GroupEntity)
