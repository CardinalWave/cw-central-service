from src.data.use_cases.users.user_authenticator import UserAuthenticator
from src.data.use_cases.users.user_register import UserRegister
from src.main.composers.relations.user_group_composer import user_group_composer
from src.presentation.controllers.users.user_register_controller import UserRegisterController

def user_register_composer():

    auth = UserAuthenticator()
    user_group = user_group_composer
    use_case = UserRegister(auth, user_group)
    controller = UserRegisterController(use_case)

    return controller.handle
