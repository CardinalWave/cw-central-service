#pylint: disable=redefined-outer-name
import pytest
from src.domain.models.register import Register
from src.domain.models.user import User
from src.tests.data.mocks.users.user_authenticator import UserAuthenticatorSpy
from src.data.use_cases.users.user_register import UserRegister

@pytest.fixture
def mock_register():
    return Register(email='lua@outlook.com', username='Lua', password='password213')

@pytest.fixture
def mock_user():
    return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                username='Lua', email='lua@outlook.com')

def test_register(mock_register, mock_user):
    users_auth = UserAuthenticatorSpy()
    user_register = UserRegister(user_authenticator=users_auth)
    response = user_register.register(mock_register)

    assert response.get("token") == mock_user.token
    assert response.get("email") == mock_user.email
    assert response.get("username") == mock_user.username
