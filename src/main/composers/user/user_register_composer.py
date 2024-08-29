from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.data.use_cases.users.user_register import UserRegister
from src.presentation.controllers.users.user_register_controller import UserRegisterController
from src.main.logs.logs import Log


def user_register_composer():
    auth = UserAuthenticator()
    logger = Log()
    use_case = UserRegister(auth, logger)
    controller = UserRegisterController(use_case, logger)

    return controller.handle
