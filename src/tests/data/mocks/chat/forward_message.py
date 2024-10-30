#pylint: disable=too-many-arguments
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface


class ForwardMessageSpy(ForwardMessageInterface):

    def send_message(self, params: any, action: str): pass
