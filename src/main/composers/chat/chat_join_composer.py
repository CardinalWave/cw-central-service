from src.infra.db.repositories.users.users_repository import UsersRepository
from src.data.use_cases.chat.chat_join import ChatJoin
from src.data.use_cases.chat.forward_message import ForwardMessage
from src.infra.security.implementations.secure_email import SecureEmail
from src.presentation.controllers.chat.chat_join import ChatJoinController
from src.main.composers.relations.validate import validate_composer
from src.main.composers.relations.user_group_composer import user_group_composer
from src.data.use_cases.relations.user_status import UserStatus


def chat_join_composer():
    users_repository = UsersRepository()
    secure_email = SecureEmail()
    user_group = user_group_composer()
    user_status = UserStatus(user_group)
    validate = validate_composer()
    forward_message = ForwardMessage()
    use_case = ChatJoin(forward_message=forward_message,
                        user_repository=users_repository,
                        secure_email=secure_email,
                        validate=validate,
                        user_status=user_status)
    controller = ChatJoinController(use_case)

    return controller.handle