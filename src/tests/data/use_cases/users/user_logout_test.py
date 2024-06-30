#pylint: disable=redefined-outer-name
from unittest.mock import MagicMock
import pytest
from src.domain.models.user import User
from src.tests.data.mocks.users.user_authenticator import UserAuthenticatorSpy
from src.tests.infra.mocks.users_repository import UsersRepositorySpy
from src.data.use_cases.users.user_logout import UserLogout

@pytest.fixture
def mock_user():
    return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                username='Lua', email='lua@outlook.com')

def test_logout(mock_user):

    users_repo = UsersRepositorySpy()
    users_repo.remove_user = MagicMock()

    users_auth = UserAuthenticatorSpy()
    users_auth.logout = MagicMock()

    user_logout = UserLogout(users_repo, users_auth)
    user_logout.logout(mock_user)

    users_auth.logout.assert_called_once_with(mock_user)
    users_repo.remove_user.assert_called_once_with(mock_user.token)
