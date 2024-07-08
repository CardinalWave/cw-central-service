from src.data.use_cases.chat.chat_join import ChatJoin
from src.data.use_cases.chat.forward_message import ForwardMessage
from src.presentation.controllers.chat.chat_join import ChatJoinController
from src.main.composers.relations.validate import validate_composer


def chat_join_composer():
    validate = validate_composer()
    forward_message = ForwardMessage()
    use_case = ChatJoin(forward_message=forward_message,
                        validate=validate)
    controller = ChatJoinController(use_case)

    return controller.handle
