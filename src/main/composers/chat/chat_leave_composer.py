from src.data.use_cases.chat.chat_leave import ChatLeave
from src.main.composers.relations.validate import validate_composer
from src.data.use_cases.chat.forward_message import ForwardMessage
from src.presentation.controllers.chat.chat_leave import ChatLeaveController
from src.main.logs.logs import Log


def chat_leave_composer():
    validate = validate_composer()
    forward_message = ForwardMessage()
    logger = Log()
    use_case = ChatLeave(validate=validate,
                         forward_message=forward_message,
                         logger=logger)
    controller = ChatLeaveController(use_case, logger)

    return controller.handle
