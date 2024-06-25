from src.data.use_cases.user_authenticator import UserAuthenticator
from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_logout import UserLogout
from src.presentation.controllers.user_logout_controller import UserLogoutController

def user_logout_composer():
    auth = UserAuthenticator()
    repository = UsersRepository()
    use_case = UserLogout(repository, auth)
    controller = UserLogoutController(use_case)

    return controller.handle
