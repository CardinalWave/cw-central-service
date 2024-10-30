from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.infra.db.repositories.users.users_repository import UsersRepository
from src.data.use_cases.users.user_logout import UserLogout
from src.presentation.controllers.users.user_logout_controller import UserLogoutController
from src.main.logs.logs import Log


def user_logout_composer():
    auth = UserAuthenticator()
    logger = Log()
    repository = UsersRepository()
    use_case = UserLogout(repository, auth, logger)
    controller = UserLogoutController(use_case)

    return controller.handle
