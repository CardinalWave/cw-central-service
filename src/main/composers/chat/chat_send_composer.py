from src.data.use_cases.chat.chat_send import ChatSend
from src.main.composers.relations.validate import validate_composer
from src.data.use_cases.chat.forward_message import ForwardMessage
from src.presentation.controllers.chat.chat_send import ChatSendController
from src.main.composers.relations.user_group_composer import user_group_composer
from src.main.logs.logs import Log


def chat_send_composer():
    validate = validate_composer()
    logger = Log()
    user_group = user_group_composer()
    forward_message = ForwardMessage()
    use_case = ChatSend(validate=validate,
                        forward_message=forward_message,
                        user_group=user_group,
                        logger=logger)
    controller = ChatSendController(use_case, logger)

    return controller.handle
