from src.data.use_cases.user_authenticator import UserAuthenticator
from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_login import UserLogin
from src.presentation.controllers.user_login_controller import UserLoginController

def user_login_composer():
    authication = UserAuthenticator()
    repository = UsersRepository()
    use_case = UserLogin(repository, authication)
    controller = UserLoginController(use_case)

    return controller.handle
