#pylint: disable=too-many-arguments
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.session import Session
from src.domain.models.user import User
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface


class ForwardMessageSpy(ForwardMessageInterface):

    def send_message(self, user: User, group: Group, session: Session, message: Dict, action: str):
        pass
