from src.data.use_cases.chat.chat_join import ChatJoin
from src.data.use_cases.chat.forward_message import ForwardMessage
from src.presentation.controllers.chat.chat_join import ChatJoinController
from src.main.composers.relations.validate import validate_composer
from src.main.composers.relations.user_group_composer import user_group_composer


def chat_join_composer():
    user_group = user_group_composer()
    validate = validate_composer()
    forward_message = ForwardMessage()
    use_case = ChatJoin(forward_message=forward_message,
                        validate=validate,
                        user_group=user_group)
    controller = ChatJoinController(use_case)

    return controller.handle
