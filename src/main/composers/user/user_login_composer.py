from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.infra.db.repositories.users.users_repository import UsersRepository
from src.data.use_cases.users.user_login import UserLogin
from src.presentation.controllers.users.user_login_controller import UserLoginController
from src.main.logs.logs import Log


def user_login_composer():
    auth = UserAuthenticator()
    logger = Log()
    repository = UsersRepository()
    use_case = UserLogin(repository, auth, logger)
    controller = UserLoginController(use_case, logger)

    return controller.handle
