from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.infra.db.repositories.users.users_repository import UsersRepository
from src.data.use_cases.users.user_login import UserLogin
from src.presentation.controllers.users.user_login_controller import UserLoginController
from src.data.use_cases.relations.user_status import UserStatus
from src.main.composers.relations.user_group_composer import user_group_composer


def user_login_composer():
    auth = UserAuthenticator()
    repository = UsersRepository()
    user_group = user_group_composer()
    user_status = UserStatus(user_group)
    use_case = UserLogin(repository, auth, user_status)
    controller = UserLoginController(use_case)

    return controller.handle
