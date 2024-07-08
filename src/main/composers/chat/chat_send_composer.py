from src.data.use_cases.chat.chat_send import ChatSend
from src.main.composers.relations.validate import validate_composer
from src.data.use_cases.chat.forward_message import ForwardMessage
from src.presentation.controllers.chat.chat_send import ChatSendController


def chat_send_composer():
    validate = validate_composer()
    forward_message = ForwardMessage()
    use_case = ChatSend(validate=validate,
                        forward_message=forward_message)
    controller = ChatSendController(use_case)

    return controller.handle
