from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.infra.db.repositories.users.users_repository import UsersRepository
from src.data.use_cases.users.user_logout import UserLogout
from src.presentation.controllers.users.user_logout_controller import UserLogoutController
from src.main.composers.relations.user_group_composer import user_group_composer
from src.data.use_cases.relations.user_status import UserStatus

def user_logout_composer():
    auth = UserAuthenticator()
    repository = UsersRepository()
    user_compose = user_group_composer()
    user_status = UserStatus(user_compose)
    use_case = UserLogout(repository, auth, user_status)
    controller = UserLogoutController(use_case)

    return controller.handle
