from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.data.use_cases.users.user_register import UserRegister
from src.presentation.controllers.user_register_controller import UserRegisterController

def user_register_composer():

    auth = UserAuthenticator()
    use_case = UserRegister(auth)
    controller = UserRegisterController(use_case)

    return controller.handle
