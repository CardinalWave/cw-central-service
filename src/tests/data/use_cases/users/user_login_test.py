#pylint: disable=redefined-outer-name
import pytest
import uuid
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.session import Session
from src.tests.infra.mocks.users_repository import UsersRepositorySpy
from src.tests.data.mocks.users.user_authenticator import UserAuthenticatorSpy
from src.data.use_cases.users.user_login import UserLogin

@pytest.fixture
def mock_login():
    return Login(email='lua@outlook.com', password='password213')

@pytest.fixture
def mock_user():
    return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                username='Lua', email='lua@outlook.com')

@pytest.fixture
def mock_session():
    return Session(session_id=str(uuid.uuid4()), device="esp8266_01")

def test_login(mock_login, mock_user, mock_session):
    users_auth = UserAuthenticatorSpy()
    user_login = UserLogin(UsersRepositorySpy(), users_auth)
    response = user_login.login(mock_login, mock_session)

    assert response.get("token") == mock_user.token
    assert response.get("email") == mock_user.email
    assert response.get("username") == mock_user.username


def test_login_error_email(mock_login, mock_session):
    mock_login.email = 'email'

    users_auth = UserAuthenticatorSpy()
    user_status = UserStatusSpy()
    user_login = UserLogin(UsersRepositorySpy(), users_auth, user_status)

    try:
        user_login.login(mock_login, mock_session)
        assert False
    except Exception as exception:
        assert str(exception) == "Email ou senha invalido"

def test_login_error_password(mock_login, mock_session):
    mock_login.password = "777777"

    users_auth = UserAuthenticatorSpy()
    user_status = UserStatusSpy()
    user_login = UserLogin(UsersRepositorySpy(), users_auth, user_status)

    try:
        user_login.login(mock_login, mock_session)
        assert False
    except Exception as exception:
        assert str(exception) == "Email ou senha invalido"

def test_login_user_loged(mock_login, mock_session):
    mock_login.email = 'lua2@outlook.com'

    users_auth = UserAuthenticatorSpy()
    user_status = UserStatusSpy()
    user_login = UserLogin(UsersRepositorySpy(), users_auth, user_status)

    try:
        user_login.login(mock_login, mock_session)
        assert False
    except Exception as exception:
        assert str(exception) == "Usuario logado"
