from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.infra.db.repositories.users.users_repository import UsersRepository
from src.data.use_cases.users.user_login import UserLogin
from src.presentation.controllers.users.user_login_controller import UserLoginController

def user_login_composer():
    auth = UserAuthenticator()
    repository = UsersRepository()
    use_case = UserLogin(repository, auth)
    controller = UserLoginController(use_case)

    return controller.handle
